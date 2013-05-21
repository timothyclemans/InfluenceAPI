from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User
import re
from django.utils import simplejson
from models import Rule, Test

def index(request):
    return render(request, 'harshstartup_converter/harshstartup_converter.html', {'inputs': Test.objects.all().values_list('input', flat=True)})

def get_conversion(request):
    """
    I: You're not being nice to me.
    O: I want to be treated nicely.

    I: You're not being kind to me.
    O: I want to be treated kindly.

    I: You're not being friendly to me.
    O: I want to be treated as a friend.

    I: You're not doing what you're told to do.
    O: I want my orders to be followed.
    """
    paragraph = request.POST['input']
    print 'Paragraph: ', paragraph
    new_paragraph = paragraph
    #phrase_conversions = [("You're not being (?P<word>\w+) to me.", "I want to be treated {{ word }}ly."), ("You're not (?P<what>[\w\s]+).", 'I want to {{ what }}.'), ("(?P<word>[\w]+)ing", "{{ word }}"), ("treated (?P<word>\w+)lyly", "treated as a {{ word }}"), ("to do what you.re told to do", "my orders to be followed")]
    phrase_conversions = Rule.objects.root_nodes().order_by('order').values_list('pattern', 'replacement')
    for phrase_conversion in phrase_conversions:
        m = re.search(phrase_conversion[0], new_paragraph)
        if m:
            print 'yes m'
            replacement = phrase_conversion[1]
            for group in m.groupdict().keys():
                print group
                replacement = replacement.replace('{{ %s }}' % (group), m.group(group))
            new_paragraph = new_paragraph.replace(m.group(), replacement)   
            break
    response_data = {}
    response_data['output'] = new_paragraph
    return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")

def edit(request):
    return render(request, 'harshstartup_converter/edit.html', {'rules': Rule.objects.root_nodes().order_by('order')})

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

def generate_pattern_and_replacement(request):
    response_data = {}
    response_data['pattern'], response_data['replacement'] = get_pattern_and_replacement(request.POST['input'], request.POST['output'])
    return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")

def save(request):
    print 'POST: ', request.POST
    for i in request.POST.items():
        print i
        if i[0].startswith('rule'):
            rule_id = re.search('rule_(?P<id>\d+)', i[0]).group('id')
            rule = Rule.objects.get(id=rule_id)
            if i[0].endswith('pattern'):
                rule.pattern = i[1]
            else:
                rule.replacement = i[1]
            rule.save()
        else:
            test_id = re.search('test_(?P<id>\d+)', i[0]).group('id')
            test = Test.objects.get(id=test_id)
            if i[0].endswith('input'):
                test.input = i[1]
            else:
                test.output = i[1]
            test.save()
    response_data = {}
    return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")

def save_test(request):
    print 'POST: ', request.POST
    test = Test(input=request.POST['input'], output=request.POST['output'])
    test.save()
    if request.POST['pattern']:
        rule = Rule(pattern=request.POST['pattern'], replacement=request.POST['replacement'])
        rule.save()
        test.rule = rule
        test.save()
    response_data = {}

    return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")
