from django.conf.urls.defaults import *


urlpatterns = patterns('',
        (r'^today/$', 'diary.views.today'),
        (r'^add_event/$', 'diary.views.add_event'),
        (r'^plusorminus/$', 'diary.views.plus_or_minus'),
)

