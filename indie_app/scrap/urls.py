from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from tastypie.api import Api

# Add resource to use here
from api.product.allproducts_resources import ProductResource
from api.website.allwebsite_resources import WebsiteResource

from scrap.views import trademark_site

###########################
v1_api = Api(api_name='v1')
v2_api = Api(api_name='v2')
###########################

# Register resource here
v1_api.register( ProductResource() )
v2_api.register( WebsiteResource() )


######################################
urlpatterns = patterns('',
    url(r'^_internal-productall-api/', include(v1_api.urls)),

    url(r'^_internal-website-api/', include(v2_api.urls)),
    url(r'^_internal/trademark/', trademark_site, name='scape_site'),
)
