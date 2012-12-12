from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'amour.views.index'),
    url(r'^training', 'amour.views.training'),
    url(r'^single', 'amour.views.single'),
    url(r'^extend', 'amour.views.extend'),
    url(r'^analysis', 'amour.views.analysis'),
)
