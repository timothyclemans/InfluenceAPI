from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User
import re
from django.utils import simplejson
from models import DailyGoal, DailyGoalStatus

def index(request):
    context = {}
    context['goal_statements'] = DailyGoal.objects.filter(user=request.user)
    context['goal_status_for_dates'] = []
    # get dates
    dates = sorted(list(set(DailyGoalStatus.objects.all().values_list('date', flat=True))))[::-1]
    last_date = dates[0] 
    import datetime
    def daterange(start_date, end_date):
        l = []
        for n in range(int ((end_date - start_date).days + 1)):
            l.append(start_date + datetime.timedelta(n))
        return l
 

    now = datetime.date.today()
    daterange = daterange(last_date, now)[1:][::-1]
    context['daterange'] = daterange
    for date in dates:
        statuses = []
        for i in context['goal_statements']:
            if DailyGoalStatus.objects.filter(daily_goal=i, date=date):
                statuses.append(DailyGoalStatus.objects.filter(daily_goal=i, date=date)[0])
            else:
                statuses.append({'exists': True, 'daily_goal': i})
        context['goal_status_for_dates'].append({'date': date, 'statuses': statuses}) 
    return render(request, 'goals/daily_goals_status.html', context)

def set_status(request):
    print request.POST
    from datetime import date
    daily_goal = DailyGoal.objects.get(id=request.POST['goal_id'])
    thedate = request.POST['date'].split('-')
    print thedate
    thedate = date(int('20'+ thedate[2]), int(thedate[0]), int(thedate[1]))
    status = True if request.POST['status'] == 'true' else False
    daily_goal_status = DailyGoalStatus(daily_goal=daily_goal, date=thedate, status=status)
    daily_goal_status.save()
    response_data = {}
    return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")

def save_goal(request):
    daily_goal = DailyGoal(user=request.user, statement=request.POST['statement'])
    daily_goal.save()
    response_data = {}
    return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")

def delete_goal(request):
    daily_goal = DailyGoal.objects.get(id=request.POST['goal_id'])
    if daily_goal.user == request.user:
        daily_goal.delete()   
    response_data = {}
    return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")
