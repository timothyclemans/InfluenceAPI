from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'influenceapi.views.home', name='home'),
    # url(r'^influenceapi/', include('influenceapi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^decisions/$', 'decisiontrees.views.decisions'),
    url(r'^decisions/(?P<id>\d+)/$', 'decisiontrees.views.decisions'),
    url(r'^harshstartup_converter/', include('harshstartup_converter.urls')),
    url(r'^goals/', include('goals.urls')),
    url(r'^marriage/', include('marriage.urls')),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
