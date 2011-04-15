from django.views.generic.simple import direct_to_template

__author__ = 'ceposta'
from django.conf.urls.defaults import *

urlpatterns = patterns("",
    url(r'^$', direct_to_template, {"template": "about/about.html"}, name="about"),
    url(r'^terms/$', direct_to_template, {"template": "about/terms.html"}, name="terms"),
    url(r'^privacy/$', direct_to_template, {"template": "about/privacy.html"}, name="privacy_policy"),
)
  