from django.conf.urls.defaults import *


urlpatterns = patterns('',
        (r'^login/$', 'accounts.views.login_user'),
)

