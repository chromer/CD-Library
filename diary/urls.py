from django.conf.urls.defaults import *


urlpatterns = patterns('',
        (r'^today/$', 'diary.views.today'),
        (r'^plusorminus/$', 'diary.views.plus_or_minus'),
        (r'^search/$', 'diary.views.search_events'),
)

