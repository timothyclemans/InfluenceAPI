from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import views 

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^replace_words/$', views.replace_words),
    url(r'^replace_words_api/$', views.replace_words_api),
)
