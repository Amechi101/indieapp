# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from _backend_api.models import Brand

AUTH_USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")

class Subscription(models.Model):
    """
    Following brands for registered users only
    """
    brand = models.ForeignKey(Brand)
    user = models.ForeignKey(AUTH_USER_MODEL)
    
    date_added = models.DateTimeField(auto_now_add=True, verbose_name=_('Date added'))

    #Metadata
    class Meta: 
        verbose_name = _('User Subscribed Brand')
        verbose_name_plural = _('User Subscribed Brands')

    def __unicode__(self):
        return "{0}".format( self.brand )
    
  



