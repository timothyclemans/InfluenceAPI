
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User
import re
from django.utils import simplejson
from models import Marriage

def index(request):
    context = {}
    
    return render(request, 'marriage/index.html', context)

def love_map(request):
    context = {}
    context['spouse'] = Marriage.objects.get(user=request.user).spouse
    return render(request, 'marriage/love_map.html', context)

def foundness_and_admiration(request):
    context = {}
    
    return render(request, 'marriage/foundness_and_admiration.html', context)
    
def turn_toward(request):
    context = {}
    
    return render(request, 'marriage/turn_toward.html', context)
    
def accept_influence(request):
    context = {}
    
    return render(request, 'marriage/accept_influence.html', context)
    
def solve_solvable_problems(request):
    context = {}
    
    return render(request, 'marriage/solve_solvable_problems.html', context)

def solve_typical_problems(request):
    context = {}
    
    return render(request, 'marriage/solve_typical_problems.html', context)

def solve_typical_problems_stress(request):
    context = {}
    
    return render(request, 'marriage/solve_typical_problems_stress.html', context)
    
def solve_typical_problems_relations_with_in_laws(request):
    context = {}
    
    return render(request, 'marriage/solve_typical_problems_relations_with_in_laws.html', context)
    
def solve_typical_problems_money(request):
    context = {}
    
    return render(request, 'marriage/solve_typical_problems_money.html', context)
    
def solve_typical_problems_sex(request):
    context = {}
    
    return render(request, 'marriage/solve_typical_problems_sex.html', context)
    
def solve_typical_problems_housework(request):
    context = {}
    
    return render(request, 'marriage/solve_typical_problems_housework.html', context)
    
def solve_typical_problems_becoming_parents(request):
    context = {}
    
    return render(request, 'marriage/solve_typical_problems_becoming_parents.html', context)
    
def overcome_gridlock(request):
    context = {}
    
    return render(request, 'marriage/overcome_gridlock.html', context)
    
def create_shared_meaning(request):
    context = {}
    
    return render(request, 'marriage/create_shared_meaning.html', context)

