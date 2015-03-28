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
	messages = {
        "brand_follow": {
            "level": messages.SUCCESS,
            "text": _("Brand was followed.")
        },
    }
	
	def get(self, request, *args, **kwargs):
		self.object = self.get_object(queryset=Brand.objects.all())

		if self.messages.get("brand_follow"):
			messages.add_message(
				self.request,
				self.messages["brand_follow"]["level"],
				self.messages["brand_follow"]["text"]
			)
		
		return super(BrandDetailView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(BrandDetailView, self).get_context_data(**kwargs)
		
		context['brand'] = self.object
		context['is_followed'] = Subscription.objects.filter(brand=self.object).count()
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
		
		return context

	def get_queryset(self,  **kwargs):
		return self.object


class BrandArchiveView( ListView):
	
	template_name = 'brands/_brandarchive.html'
	model = Brand
	
	def get_context_data(self, **kwargs):
		context = super(BrandArchiveView, self).get_context_data(**kwargs)
		context['brand_list_archive'] = Brand.objects.filter(brand_state=False).order_by('brand_name')
		
		return context




		

