from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from tastypie.api import Api

# Add resource to use here
from api.resources import ProductResource
from scrap.views import trademark_site

###########################
v1_api = Api(api_name='v1')
###########################

# Register resource here
v1_api.register( ProductResource() )

######################################
urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^_internal/trademark/', trademark_site, name='scape_site'),
)
