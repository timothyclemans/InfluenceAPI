from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import views 

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^love_map/$', views.love_map),
    url(r'^foundness_and_admiration/$', views.foundness_and_admiration),
    url(r'^turn_toward/$', views.turn_toward),
    url(r'^accept_influence/$', views.accept_influence),
    url(r'^solve_solvable_problems/$', views.solve_solvable_problems),
    url(r'^solve_solvable_problems/typical_problems/$', views.solve_typical_problems),
    url(r'^solve_solvable_problems/typical_problems/stress/$', views.solve_typical_problems_stress),
    url(r'^solve_solvable_problems/typical_problems/relations_with_in_laws/$', views.solve_typical_problems_relations_with_in_laws),
    url(r'^solve_solvable_problems/typical_problems/money/$', views.solve_typical_problems_money),
    url(r'^solve_solvable_problems/typical_problems/sex/$', views.solve_typical_problems_sex),
    url(r'^solve_solvable_problems/typical_problems/housework/$', views.solve_typical_problems_housework),
    url(r'^solve_solvable_problems/typical_problems/becoming_parents/$', views.solve_typical_problems_becoming_parents),
    url(r'^overcome_gridlock/$', views.overcome_gridlock),
    url(r'^create_shared_meaning/$', views.create_shared_meaning),
)
