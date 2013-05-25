from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User
import re
from django.utils import simplejson
from models import Rule, Test
from patterns_replacements import get_pattern_and_replacement

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
    new_paragraph = paragraph.strip()
    phrase_conversions = Rule.objects.root_nodes().order_by('order').values_list('pattern', 'replacement')
    for phrase_conversion in phrase_conversions:
        pattern = phrase_conversion[0].replace('?', '\?').replace('\?P', '?P')
        m = re.search('^' + pattern + '$', new_paragraph)
        if m:
            print 'yes m'
            print phrase_conversion[0]
            print m.groupdict()
            replacement = phrase_conversion[1]
            for group in sorted(m.groupdict().keys()):
                print group
                replacement = replacement.replace('{{ %s }}' % (group), m.group(group))
                print replacement
            new_paragraph = new_paragraph.replace(m.group(), replacement)  
            #new_paragraph = new_paragraph.replace('??', '?') 
            break
    response_data = {}
    response_data['output'] = new_paragraph
    return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")

def edit(request):
    return render(request, 'harshstartup_converter/edit.html', {'rules': Rule.objects.root_nodes().order_by('order')})

def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]

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
    rule = None
    if request.POST['pattern']:
        rule = Rule(pattern=request.POST['pattern'], replacement=request.POST['replacement'])
        rule.save()
    if rule:
        test = Test(input=request.POST['input'], output=request.POST['output'], rule=rule)
    else:
        test = Test(input=request.POST['input'], output=request.POST['output'])
    test.save()
    response_data = {}

    return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")

def delete_rule(request):
    rule = Rule.objects.get(id=request.POST['id'])
    rule.delete()
    response_data = {}

    return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")
