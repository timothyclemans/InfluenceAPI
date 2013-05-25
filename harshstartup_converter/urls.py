from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import views 

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^get_conversion/$', views.get_conversion),
    url(r'^edit/$', views.edit),
    url(r'^save/$', views.save),
    url(r'^save_test/$', views.save_test),
    url(r'^generate_pattern_and_replacement/$', views.generate_pattern_and_replacement),
    url(r'^delete_rule/$', views.delete_rule),
)
