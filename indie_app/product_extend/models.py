# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal
from product_extend.utils.fields import CurrencyField

import datetime

from website.models import Website

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Product(models.Model):
    """
    The product structure for the application, the products we scrap from sites will model this and save directly into the tables.
    """

    product_name = models.CharField(max_length=254, verbose_name=_('Name'), null=True, blank=True)
    
    product_price = CurrencyField( verbose_name=_('Unit price') )
    product_slug_url = models.URLField(max_length=200,  null=True, blank=True)
    product_category = models.CharField(max_length=254, blank=True, null=True)

    # Points to a Cloudinary image
    product_image = CloudinaryField('product image', null=True, blank=True)
    
    product_website_name = models.CharField(max_length=254, blank=True, null=True)
    
    #For Admin Purposes, to keep track of new and old items in the database by administrative users
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('Date added'))
    last_modified = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last modified') )

    #For Admin Purposes, to make sure an item is active by administrative users
    active = models.BooleanField(default=True, verbose_name=_('Active') )

    # Foreign Key
    website = models.ForeignKey(Website, null=True)

    #Metadata
    class Meta: 
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __unicode__(self):
        return "{0}".format(self.product_name)


    def get_product_price(self):
        """
        Return the price for this item (provided for extensibility)
        """
        return "{0}".format(self.product_price)

    def get_product_name(self):
        """
        Return the name of this Product (provided for extensibility)
        """
        return "{0}".format(self.product_name)


    def get_product_website_name(self):
        """
        Return the website's name for this item (provided for extensibility)
        """
        return "{0}".format(self.product_website_name)

    def get_product_slug_url(self):
        """
        Return the product slug url for this item (provided for extensibility)
        """
        return "{0}".format(self.product_slug_url)

    def get_product_category(self):
        """
        Return the product category for this item (provided for extensibility)
        """
        return "{0}".format(self.product_category)


















