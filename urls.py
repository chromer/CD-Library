from django.conf.urls.defaults import *
from settings import DEBUG

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^djen_project/', include('djen_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('accounts.urls')),
)

if DEBUG:
    urlpatterns += patterns('', (
        r'^static_media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': 'static_media'}
    ))

