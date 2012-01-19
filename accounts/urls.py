from django.conf.urls.defaults import *


urlpatterns = patterns('',
        (r'^login/$', 'accounts.views.login_user'),
        (r'^signup/$', 'accounts.views.signup'),
)

