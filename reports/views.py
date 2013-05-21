from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from superpowers.models import Superpower
from django.contrib.auth.models import User

def bucks_given(request):
    
    return render(request, 'reports/bucks_given.html', {'superpowers': Superpower.objects.all(), 'students': User.objects.all()})
