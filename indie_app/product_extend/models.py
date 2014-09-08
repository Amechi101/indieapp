from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from shop.models import Product

import datetime
import imghdr # Used to validate images
import urllib2 # Used to download images
import urlparse # Cleans up image urls
import cStringIO # Used to imitate reading from byte file
from PIL import Image # Holds downloaded image and verifies it
import copy # Copies instances of Image


class ProductExtend(Product):
    label_name = models.CharField(max_length=254, blank=True, null=True)
    product_website_name = models.CharField(max_length=254, blank=True, null=True)
    product_website = models.URLField(max_length=200,  null=True, blank=True) 
    product_img = models.ImageField('Product Image', upload_to='product_images', null=True, blank=True) 

    #Metadata
    class Meta: 
    	pass

    #Helps return something meaningful, to show within the admin interface for easy interaction
    def get_label_name(self):
        """
        Return the label name for this item (provided for extensibility)
        """
        return "{0}".format(self.label_name)

    def get_product_website_name(self):
        """
        Return the proudct website name for this item (provided for extensibility)
        """
        return "{0}".format(self.product_website_name)
    
    def get_product_website(self):
    	"""
        Return the product website for this item (provided for extensibility)
        """
        return "{0}".format(self.product_website)

    # From http://ishcray.com/downloading-and-saving-image-to-imagefield-in-django #################################
    # For image saving and other features
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

def download_image(url):
	"""Downloads an image and makes sure it's verified.
 
    Returns a PIL Image if the image is valid, otherwise raises an exception.
    """

	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'} # More likely to get a response if server thinks you're a browser
	r = urllib2.Request(url, headers=headers)
	request = urllib2.urlopen(r, timeout=10)
	image_data = cStringIO.StringIO(request.read())
	img = Image.open(image_data)
	img_copy = copy.copy(img)
	if vaild_img(img_copy):
		return img
	else:
		raise Exception('An invalid image was detected when attempting to save a Product!')

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
# END ################################

















