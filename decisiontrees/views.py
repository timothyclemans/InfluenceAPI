from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from models import Decision
from django.contrib.auth.models import User

def decisions(request, id=0):
    decisions = Decision.objects.get(id=id).get_children() if id else Decision.objects.root_nodes() 
    main_decision = Decision.objects.get(id=id) if id else ''
    decisions_needing_explanation = []
    for decision in Decision.objects.all():
        if not decision.get_children() and not decision.explanation:
            decisions_needing_explanation.append(decision)
    return render(request, 'decisiontrees/decisions.html', {'decisions': decisions, 'main_decision': main_decision, 'decisions_needing_explanation': decisions_needing_explanation})
