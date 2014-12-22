# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal
from product_extend.utils.fields import CurrencyField

import datetime

import imghdr # Used to validate images
import urllib2 # Used to download images
import urlparse # Cleans up image urls
import cStringIO # Used to imitate reading from byte file
from PIL import Image # Holds downloaded image and verifies it
import copy # Copies instances of Image

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
    product_img = models.ImageField('Product Image', upload_to='product_images', null=True, blank=True) 
    
    product_website_url = models.URLField(max_length=200,  null=True, blank=True) 
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
    
    def get_product_website_url(self):
    	"""
        Return the website's url for this item (provided for extensibility)
        """
        return "{0}".format(self.product_website_url)

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

    # From http://ishcray.com/downloading-and-saving-image-to-imagefield-in-django 
    def save(self, url="", *args, **kwargs):
    	if self.product_img != '' and url != '':
    		image = download_image(url)
    		try:
    			filename = urlparse.urlparse(url).path.split('/')[-1]
    			self.product_img = filename
    			tempfile = image 
    			tempfile_io = cStringIO.StringIO()
    			tempfile.save(tempfile_io, format=image.format)
    			self.product_img.save(filename, ContentFile(tempfile_io.getvalue()), save=False )
    		except Exception, e:
    			print("Error trying to save model: saving image failed: " + str(e))
    			pass
    	super(Product, self).save(*args, **kwargs)



# From http://ishcray.com/downloading-and-saving-image-to-imagefield-in-django 
def download_image(url):
	"""Downloads an image and makes sure it's verified.
 
    Returns a PIL Image if the image is valid, otherwise raises an exception.
    """

	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'} 
	r = urllib2.Request(url, headers=headers)
	request = urllib2.urlopen(r, timeout=10)
	image_data = cStringIO.StringIO(request.read())
	img = Image.open(image_data)


	img_copy = copy.copy(img)
	if vaild_img(img_copy):
		return img
	else:
		raise Exception('An invalid image was detected when attempting to save!')

# From http://ishcray.com/downloading-and-saving-image-to-imagefield-in-django 
def valid_img(img):
	"""Verifies that an instance of a PIL Image Class is actually an image and returns either True or False."""
	type = img.format
	if type in ('GIF', 'JPEG', 'JPG', 'PNG'):
		try:
			img.verify()
			return True
		except:
			return False
	else:
		return True


















