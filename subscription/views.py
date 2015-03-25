# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, get_object_or_404, render_to_response

from django.core.urlresolvers import reverse
from django.shortcuts import render


from subscription.models import Subscription
from _backend_api.models import Brand
from subscription.managers import SubscriptionManager

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)






class SubscriptionListView(LoginRequiredMixin, View):	
	def get(self, request):
		brands = Subscription.objects.filter(brands=request.user)
		return render_to_response("account/account_features/_user_brands.html", {"brands": brands})
		
class SubscribeView(LoginRequiredMixin, View):
	def get(self, request):
		SubscriptionManager().subscribe(brand=get_object_or_404(Brand, brand_name=request.GET.get("brand_name") ),user=request.user)

		if request.GET.get("ajax"):
			return HttpResponse('ok')
		return HttpResponseRedirect("/account/subscribed-brands/?added=")

class UnsubscribeView(LoginRequiredMixin, View):	
	def get(self, request):
		SubscriptionManager.unsubscribe(brand=get_object_or_404(name=request.GET.get("brand_name"), user=request.user))
		return HttpResponse("ok")
		
	def post(self, request):
		SubscriptionManager.unsubscribe(brand=get_object_or_404(name=request.POST.get("brand_name"), user=request.user))
		return HttpResponse("ok")
		

