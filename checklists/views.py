from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from models import ChecklistTemplate
from django.contrib.auth.models import User

def checklist(request, id):
    
    return render(request, 'checklists/checklist.html', {'checklist': ChecklistTemplate.objects.get(id=id)})
