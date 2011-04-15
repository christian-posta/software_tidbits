from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'tidbits.views.homepage', name="home"),
    url(r'^about/', include("about.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tidbits/', include("tidbits.urls")),
    url(r"", include("staticfiles.urls")),

)
