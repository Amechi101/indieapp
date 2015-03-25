# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.shortcuts import render

from django.views.generic import View


from subscription.models import Subscription
from _backend_api.models import Brand
from subscription.managers import SubscriptionManager

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


# @login_required
# def account_subscribe( request ):   
  
# 	brands = Subscription.objects.filter(brands=request.user)
# 	return render_to_response("account/account_features/_user_brands.html", {"brands": brands})


# @login_required
# def subscribe( request ):
# 	SubscriptionManager().subscribe(brand=get_object_or_404(Brand, brand_name=request.GET.get("brand_name") ),user=request.user)

# 	if request.GET.get("ajax"):
# 		return HttpResponse('ok')
# 	return HttpResponseRedirect("/account/subscribed-brands/?added=")


# @login_required
# def unsubscribe( request ):
# 	SubscriptionManager.unsubscribe(brand=get_object_or_404(name=request.GET.get("brand_name"), user=request.user))
# 	return HttpResponse("ok")


class SubscriptionListView(LoginRequiredMixin, View):	
	def get(self, request):
		brands = Subscription.objects.filter(brand=request.user)
		return render_to_response("account/account_features/_user_brands.html", {"brands": brands})

class UnsubscriveView(LoginRequiredMixin, View):	
	def get(self, request):
		SubscriptionManager.unsubscribe(brand=get_object_or_404(name=request.GET.get("brand_name"), user=request.user))
		return HttpResponse("ok")
		

