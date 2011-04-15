__author__ = 'ceposta'

from django.conf.urls.defaults import *

urlpatterns = patterns("",
    url(r'^create/$', "tidbits.views.create_tidbit", name="create_tidbit"),
    url(r'^mine/$', "tidbits.views.my_tidbits",  name="show_my_tidbits"),
)