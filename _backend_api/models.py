# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal
from _backend_api.utils.fields import CurrencyField

import datetime

class Brand(models.Model):
    designers_name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    
    brand_name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    brand_founded = models.IntegerField(max_length=4, null=True)
    
    brand_origin_city = models.CharField(max_length=255, blank=True, null=True)
    brand_origin_state = models.CharField(max_length=2, blank=True, null=True)

    
    brand_description = models.TextField(null=True, blank=True)
    brand_product_description = models.TextField(null=True, blank=True)

    #Shows details about specific brand
    brand_detail_slug = models.SlugField(max_length=255, verbose_name=_('Brand Slug'), unique=True,  null=True,  blank=True)
    
    brand_logo = CloudinaryField('Logo Image', null=True, blank=True)
    brand_feature_image = CloudinaryField('Featured Brand Image', null=True, blank=True)

    menswear = models.BooleanField(default=False, verbose_name=_('Menswear'))
    womenswear = models.BooleanField(default=False, verbose_name=_('Womenswear'))
    
    active = models.BooleanField(default=True, verbose_name=_('Active'))

    #For Admin Purposes and filtering, to keep track of new and old  in the database by administrative users
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('Date added'))
    last_modified = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last modified'))

    #Metadata
    class Meta: 
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __unicode__(self):
        return "{0}".format( self.brand_name )

    #Helps return something meaningful, to show within the admin interface for easy interaction
    def get_designers_name(self):
        """
        Return item (provided for extensibility)
        """
        return "{0}".format(self.designers_name)
    
    def get_brand_name(self):
        """
        Return item (provided for extensibility)
        """
        return "{0}".format(self.brand_name)

    def get_brand_name(self):
        """
        Return item (provided for extensibility)
        """
        return "{0}".format(self.brand_name)
    
    def get_brand_founded(self):
        """
        Return item (provided for extensibility)
        """
        return "{0}".format(self.brand_founded)

    def get_brand_origin_city(self):
        """
        Return item (provided for extensibility)
        """
        return "{0}".format(self.brand_origin_city)

    def get_brand_origin_state(self):
        """
        Return item (provided for extensibility)
        """
        return "{0}".format(self.brand_origin_state)

    def get_brand_description(self):
        """
        Return item (provided for extensibility)
        """
        return "{0}".format(self.brand_description)

    def get_brand_product_description(self):
        """
        Return item (provided for extensibility)
        """
        return "{0}".format(self.brand_product_description)
    
    def get_absolute_url(self):
        return reverse('brand_detail', args=[self.brand_detail_slug])


class Product(models.Model):
    """
    The product structure for the application, the products we scrap from sites will model this and save directly into the tables.
    """

    product_name = models.CharField(max_length=255, verbose_name=_('Product Name'), null=True, blank=True)
    product_price = CurrencyField( verbose_name=_('Unit price') )

    # Points to a Cloudinary image
    product_image = CloudinaryField('product image', max_length=255, null=True, blank=True)
    
    #For Admin Purposes, to keep track of new and old items in the database by administrative users
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('Date added'))
    last_modified = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last modified') )

    #For Admin Purposes, to make sure an item is active by administrative users
    active = models.BooleanField(default=True, verbose_name=_('Active') )

    # Foreign Key
    brand = models.ForeignKey(Brand, null=True)

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


class Location(models.Model):
    contact_type = models.CharField(max_length=255, blank=True, null=True)
    
    brand_address = models.CharField(max_length=255, blank=True, null=True)
    brand_city = models.CharField(max_length=50, null=True, blank=True)
    brand_state = models.CharField(max_length=2, null=True, blank=True)

    brand_website_name = models.CharField(max_length=255, blank=True, null=True)
    brand_website_url = models.URLField(max_length=200, null=True, blank=True)

    brand_email = models.CharField(max_length=255, blank=True, null=True)

    brand_email_state = models.BooleanField(default=False, verbose_name=_('Email State'))

    #Foreign Keys
    brand = models.ForeignKey(Brand, null=True)
    
    #Metadata
    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")
    
    #Helps return something meaningful, to show within the admin interface for easy interaction
    def __unicode__(self):
        return "{0}".format(self.brand)

    def get_contact_type(self):
        """
        Return this item (provided for extensibility)
        """
        return "{0}".format(self.contact_type)

    def get_brand_address(self):
        """
        Return this item (provided for extensibility)
        """
        return "{0}".format(self.brand_address)

    def get_brand_city(self):
        """
        Return this item (provided for extensibility)
        """
        return "{0}".format(self.brand_city)

    def get_brand_state(self):
        """
        Return this item (provided for extensibility)
        """
        return "{0}".format(self.brand_state)

    def get_brand_website_name(self):
        """
        Return this item (provided for extensibility)
        """
        return "{0}".format(self.brand_website_name)

    def get_brand_website_url(self):
        """
        Return this item (provided for extensibility)
        """
        return "{0}".format(self.brand_website_url)

    def get_brand_email(self):
        """
        Return this item (provided for extensibility)
        """
        return "{0}".format(self.brand_email)




















