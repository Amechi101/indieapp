from __future__ import unicode_literals 

from django.utils.translation import ugettext_lazy as _
from django.contrib import auth, messages

from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from _backend_api.models import Product, Brand, Location

from subscription.models import Subscription
from subscription.managers import SubscriptionManager

class BrandDetailView(SingleObjectMixin, ListView):
	
	template_name = 'brands/_brandguide.html'
	
	def get(self, request, *args, **kwargs):
		self.object = self.get_object(queryset=Brand.objects.all())

		return super(BrandDetailView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):

		ctx = super(BrandDetailView, self).get_context_data(**kwargs)
		
		ctx['brand'] = self.object
		ctx['is_followed'] = Subscription.objects.filter(brand=self.object, user=self.request.user.id).count()
		ctx['product_list'] = Product.objects.filter(brand=self.object)
		ctx['address_list'] = Location.objects.filter(brand=self.object)
		
		return ctx

	def get_queryset(self,  **kwargs):
		return self.object


class BrandCollectionView(SingleObjectMixin, ListView):
	
	template_name = 'brands/_brandcollection.html'
	context_object_name = 'brand_collection'

	def get(self, request, *args, **kwargs):
		self.object = self.get_object(queryset=Brand.objects.all())
		
		return super(BrandCollectionView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		
		ctx = super(BrandCollectionView, self).get_context_data(**kwargs)
		
		ctx['brand'] = self.object
		ctx['product_list'] = Product.objects.filter(brand=self.object)
		
		return ctx

	def get_queryset(self,  **kwargs):
		return self.object


class BrandArchiveView( ListView ):
	
	template_name = 'brands/_brandarchive.html'
	model = Brand
	
	def get_context_data(self, **kwargs):

		ctx = super(BrandArchiveView, self).get_context_data(**kwargs)
		ctx['brand_list_archive'] = Brand.objects.filter(brand_state=True).order_by('brand_name')
		
		return ctx




		

