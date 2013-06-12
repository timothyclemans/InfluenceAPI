from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User
import re
from django.utils import simplejson
from models import WordReplacement

def index(request):
    context = {}
    return render(request, 'profiles/index.html', context)

def replace_words(request):
    context = {}
    return render(request, 'profiles/replace_words.html', context)

def replace_words_api(request):
    word_replacements = WordReplacement.objects.all().values_list('word', 'replacement', 'summary')
    paragraph = request.GET['paragraph']
    for word, replacement, summary in word_replacements:
         paragraph = paragraph.replace(word, '<span title="%s" style="background:yellow;">%s</span>' % (summary, replacement))
    response_data = {'paragraph': paragraph}
    return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")
