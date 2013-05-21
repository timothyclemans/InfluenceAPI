from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'influenceapi.views.home', name='home'),
    # url(r'^influenceapi/', include('influenceapi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^decisions/$', 'decisiontrees.views.decisions'),
    url(r'^decisions/(?P<id>\d+)/$', 'decisiontrees.views.decisions'),
    url(r'^harshstartup_converter/', include('harshstartup_converter.urls')),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
