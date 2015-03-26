from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from tastypie.api import Api

# Add resource to use here
from api.brands.allbrands_resources import BrandResource

from _backend_api.views import BrandDetailView, BrandArchiveView, BrandCollectionView

###########################
v1_api = Api(api_name='v1')
v1_api.register( BrandResource() )
###########################


urlpatterns = patterns('',
	# Api resource
    url(r'^_internal_brandall_api/$', include(v1_api.urls)),
	
	url(r'^(?P<slug>[\w\d-]+)/$', BrandDetailView.as_view(), name="brand_view"),
	url(r'^(?P<slug>[\w\d-]+)/collection/$', BrandCollectionView.as_view(), name="brand_collection"),
	url(r'^archive/$', BrandArchiveView.as_view(), name="brand_archive"),
)


