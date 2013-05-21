from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import re

class Rule(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    pattern = models.CharField(max_length=2000)
    replacement = models.CharField(max_length=2000)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return '%s || %s' % (self.pattern, self.replacement)

    def get_tests(self):
        return Test.objects.filter(rule=self)

def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]

def get_pattern_and_replacement(the_input, output):
    """
    Given the_input and output returns the pattern for matching more general case of the_input and a template string for generating the desired output.

    >>> get_pattern_and_replacement("You're not being nice to me.", "I want to be treated nicely.")
    ("You're not being (?P<word>\w+) to me.", "I want to be treated {{ word }}ly.")
    >>> get_pattern_and_replacement("You're not meeting my needs.", "I want my needs met.")
    ("You're not meeting my (?P<word>\w+).", "I want my {{ word }} met.")
    """
    input_set = set(flatten([[the_input[i: i + j] for i in range(len(the_input) - j) if not ' ' in the_input[i: i + j]] for j in range(3, 12)]))
    output_set = set(flatten([[output[i: i + j] for i in range(len(the_input) - j) if not ' ' in output[i: i + j]] for j in range(3, 12)]))
    
    intersection = input_set & output_set
    if intersection:
        intersection = list(intersection)
        intersection = sorted(intersection, key=lambda x: len(x))[::-1]
        print intersection
        pattern = the_input.replace(intersection[0], '(?P<word>\w+)')
        replacement = output.replace(intersection[0], '{{ word }}')
        return (pattern, replacement)
    else:
        return (the_input, output)

class Test(models.Model):
    rule = models.ForeignKey(Rule, null=True, blank=True)
    input = models.CharField(max_length=2000)
    output = models.CharField(max_length=2000)   

    def __unicode__(self):
        return '%s || %s' % (self.input, self.output)

    def save(self):
        if not self.rule:
            pattern, replacement = get_pattern_and_replacement(self.input, self.output)
            if not Rule.objects.filter(pattern=pattern):
                rule = Rule(pattern=pattern, replacement=replacement)
                rule.save()
            else:
                rule = Rule.objects.filter(pattern=pattern)[0]
            self.rule = rule
        super(Test, self).save()

    def test_passes(self):
        new_paragraph = self.input 
        #phrase_conversions = [("You're not being (?P<word>\w+) to me.", "I want to be treated {{ word }}ly."), ("You're not (?P<what>[\w\s]+).", 'I want to {{ what }}.'), ("(?P<word>[\w]+)ing", "{{ word }}"), ("treated (?P<word>\w+)lyly", "treated as a {{ word }}"), ("to do what you.re told to do", "my orders to be followed")]
        phrase_conversions = Rule.objects.root_nodes().order_by('order').values_list('pattern', 'replacement')
        for phrase_conversion in phrase_conversions:
            m = ''
            try:
                m = re.search(phrase_conversion[0], new_paragraph)
            except:
                print 'Bad: ', phrase_conversion[0]
            if m:
                print 'yes m'
                replacement = phrase_conversion[1]
                for group in m.groupdict().keys():
                    print group
                    replacement = replacement.replace('{{ %s }}' % (group), m.group(group))
                new_paragraph = new_paragraph.replace(m.group(), replacement)   
                break
        print (new_paragraph == self.output, new_paragraph, self.output)
        return (new_paragraph == self.output, new_paragraph, self.output)
        
