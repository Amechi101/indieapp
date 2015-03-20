from __future__ import unicode_literals 

from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView
from _backend_api.models import Brand

class HomepageView(ListView):

	template_name = 'homepage.html'
	
	model = Brand

	def get_context_data(self, **kwargs):
		context = super(HomepageView, self).get_context_data(**kwargs)
		context['brand_list'] = Brand.objects.filter(brand_state=True).order_by('brand_name')
		
		return context