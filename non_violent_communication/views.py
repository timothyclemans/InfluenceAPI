from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User
import re
from django.utils import simplejson

def index(request):
    context = {}
    
    return render(request, 'non_violent_communication/index.html', context)
