from __future__ import unicode_literals 


from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication
from tastypie import fields
from tastypie.resources import ModelResource, ALL


from product_extend.models import Product



class ProductResource(ModelResource):
	"""
	access to the product database is available here
	"""
    
	class Meta:
		
		queryset = Product.objects.all()
		resource_name = 'all'
		limit = 50
		allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
		authentication = BasicAuthentication()
		authorization = DjangoAuthorization()
		filtering = {
		    'product_name': ALL
		}






