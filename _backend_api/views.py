from __future__ import unicode_literals 

from django.utils.translation import ugettext_lazy as _

from django.views.generic import ListView
from django.core.urlresolvers import reverse
from django.views.generic.detail import SingleObjectMixin

from _backend_api.models import Product, Brand, Location

class BrandDetailView(SingleObjectMixin, ListView):
	
	template_name = 'brands/_brandguide.html'
	
	def get(self, request, *args, **kwargs):
		self.object = self.get_object(queryset=Brand.objects.all())
		
		return super(BrandDetailView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(BrandDetailView, self).get_context_data(**kwargs)
		
		context['brand'] = self.object
		context['product_list'] = Product.objects.filter(brand=self.object)
		context['address_list'] = Location.objects.filter(brand=self.object)
		
		return context

	def get_queryset(self,  **kwargs):
		return self.object

class BrandCollectionView(SingleObjectMixin, ListView):
	
	template_name = 'brands/_brandcollection.html'
	context_object_name = 'brand_collection'



	def get(self, request, *args, **kwargs):
		self.object = self.get_object(queryset=Brand.objects.all())
		
		return super(BrandCollectionView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(BrandCollectionView, self).get_context_data(**kwargs)
		
		context['brand'] = self.object
		context['product_list'] = Product.objects.filter(brand=self.object)
		context['address_list'] = Location.objects.filter(brand=self.object)
		
		return context

	def get_queryset(self,  **kwargs):
		return self.object



class BrandArchiveView( ListView):
	
	template_name = 'brands/_brandarchive.html'
	model = Brand
	
	def get_context_data(self, **kwargs):
		context = super(BrandArchiveView, self).get_context_data(**kwargs)
		context['brand_list_archive'] = Brand.objects.filter(brand_state=True).order_by('brand_name')
		
		return context




		

