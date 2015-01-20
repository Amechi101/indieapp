from __future__ import unicode_literals 


from django.shortcuts import render, render_to_response

from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _


from django.views.generic import ListView
from website.models import Website


class WebsiteView(ListView):

	context_object_name = 'home'
	template_name = 'homepage.html'
	queryset = Website.objects.filter(active=True).order_by('name')
	paginate_by = 5
	model = Website


	def get_context_data(self, **kwargs):
		context = super(WebsiteView, self).get_context_data(**kwargs)
		return context



