from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import views 

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^update_status/$', views.set_status),
    url(r'^save_goal/$', views.save_goal),
    url(r'^delete_goal/$', views.delete_goal),
)
