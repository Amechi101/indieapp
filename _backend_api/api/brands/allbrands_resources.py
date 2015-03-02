from __future__ import unicode_literals 


from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication
from tastypie import fields
from tastypie.resources import ModelResource, ALL


from _backend_api.models import Brand



class BrandResource(ModelResource):
	"""
	access to the website database is available here
	"""
    
	class Meta:
		
		queryset = Brand.objects.all()
		resource_name = 'all_brands'
		limit = 50
		allowed_methods = ['get', 'post']
		authentication = BasicAuthentication()
		authorization = DjangoAuthorization()
		filtering = {
		    'brand_name': ALL,
            'menswear': ALL,
            'womenswear': ALL,
            'date_added': ALL,
		}
        
        ordering = [
                'date_added'
        ]






