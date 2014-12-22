from __future__ import unicode_literals 


from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _


from django.views.generic import ListView
from product_extend.models import Product



class ProductView(ListView):

	context_object_name = 'product_list'
	template_name = 'product_extend/_productlist.html'
	model = Product

	def get_context_data(self, **kwargs):
		context = super(ProductView, self).get_context_data(**kwargs)
		return context

	def get_queryset(self,  **kwargs):
		qs = super(ProductView, self).get_queryset()
		return qs.filter(website__website_slug__exact=self.kwargs['website_slug'])


		

