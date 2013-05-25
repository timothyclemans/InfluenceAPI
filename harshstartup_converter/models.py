from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import re
from patterns_replacements import get_pattern_and_replacement

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
                pattern = phrase_conversion[0].replace('?', '\?').replace('\?P', '?P')
                m = re.search('^' + pattern + '$', new_paragraph)
            except:
                print 'Bad: ', phrase_conversion[0]
            if m:
                print 'yes m'
                print phrase_conversion[0]
                replacement = phrase_conversion[1]
                for group in m.groupdict().keys():
                    print group
                    replacement = replacement.replace('{{ %s }}' % (group), m.group(group))
                new_paragraph = new_paragraph.replace(m.group(), replacement)   

                break
        print (new_paragraph == self.output, new_paragraph, self.output)
        return (new_paragraph == self.output, new_paragraph, self.output)
        
