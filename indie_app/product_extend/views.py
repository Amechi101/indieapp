from __future__ import unicode_literals 


from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _


from django.views.generic import ListView

from product_extend.models import Product



class ProductView(ListView):

	context_object_name = 'product_list'
	template_name = 'product_extend/_productlist.html'
	# queryset = ProductExtend.objects.filter(id=1)
	model = Product

	def get_context_data(self, **kwargs):
		context = super(ProductView, self).get_context_data(**kwargs)
		return context


		

