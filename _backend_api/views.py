from __future__ import unicode_literals 


from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView

from _backend_api.models import Product, Brand, Location

class BrandDetailView(ListView):

	context_object_name = 'product_list'
	template_name = 'brand_guides/_brandguide.html'
	queryset = Product.objects.all()


	def get_context_data(self, **kwargs):
		context = super(BrandDetailView, self).get_context_data(**kwargs)
		context['brand_list'] = Brand.objects.all()
		context['address_list'] = Location.objects.all()
		return context

	def get_queryset(self,  **kwargs):
		qs = super(BrandDetailView, self).get_queryset()
		return qs.filter(brand__brand_detail_slug__exact=self.kwargs['brand_detail_slug'])

class HomepageView(ListView):

	template_name = 'homepage.html'
	model = Brand

	def get_context_data(self, **kwargs):
		context = super(HomepageView, self).get_context_data(**kwargs)
		context['brand_list'] = Brand.objects.filter(active=True).order_by('brand_name')
		return context

		

