from django.conf.urls import patterns, include, url
from django.views.static import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^amour/', include("amour.urls")),
    (r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS, 'show_indexes': True}),
    # url(r'^polls/', include("polls.urls")),
    # url(r'^admin/', include(admin.site.urls)),
)
