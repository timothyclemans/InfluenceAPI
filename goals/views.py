from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User
import re
from django.utils import simplejson
from models import DailyGoal, DailyGoalStatus

def index(request):
    context = {}
    context['goal_statements'] = DailyGoal.objects.filter(user=request.user).values_list('statement', flat=True)
    context['goal_status_for_dates'] = []
    # get dates
    dates = DailyGoalStatus.objects.all().order_by('-date').values_list('date', flat=True)   
    for date in dates:
        context['goal_status_for_dates'].append({'date': date, 'statuses': DailyGoalStatus.objects.filter(date=date).values_list('status', flat=True)}) 
    return render(request, 'goals/daily_goals_status.html', context)


