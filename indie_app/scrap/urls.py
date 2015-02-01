from __future__ import unicode_literals
from django.conf.urls import patterns, include, url

from scrap._trademark_views import _trademark


urlpatterns = patterns('', 
    url(r'^_internal/trademark_api/', _trademark),
)
