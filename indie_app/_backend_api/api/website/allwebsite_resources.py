from __future__ import unicode_literals 


from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication
from tastypie import fields
from tastypie.resources import ModelResource, ALL


from _backend_api.models import Website



class WebsiteResource(ModelResource):
	"""
	access to the website database is available here
	"""
    
	class Meta:
		
		queryset = Website.objects.all()
		resource_name = 'all_wesbsites'
		limit = 50
		allowed_methods = ['get', 'post']
		authentication = BasicAuthentication()
		authorization = DjangoAuthorization()
		filtering = {
		    'name': ALL,
            'menswear': ALL,
            'womenswear': ALL,
            'date_added': ALL,
		}
        
        ordering = [
                'date_added'
        ]






