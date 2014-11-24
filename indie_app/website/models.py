from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

import datetime

import imghdr # Used to validate images
import urllib2 # Used to download images
import urlparse # Cleans up image urls
import cStringIO # Used to imitate reading from byte file
from PIL import Image # Holds downloaded image and verifies it
import copy # Copies instances of Image


class Website(models.Model):
    name = models.CharField(max_length=254, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(verbose_name=_('Website Slug'), unique=True)
    site_logo = models.ImageField('Websites Logo', upload_to='website_logo_images', null=True, blank=True) 
    active = models.BooleanField(default=False, verbose_name=_('Active'))

    #Metadata
    class Meta: 
        verbose_name = _('Website')
        verbose_name_plural = _('Websites')


    #Helps return something meaningful, to show within the admin interface for easy interaction
    def get_name(self):
        """
        Return the label name for this item (provided for extensibility)
        """
        return "{0}".format(self.name)

    def get_description(self):
        """
        Return the proudct website name for this item (provided for extensibility)
        """
        return "{0}".format(self.description)
    
    def get_absolute_url(self):
        return reverse('site_detail', args=[self.slug])

    def get_site_logo(self):
        """
        Return the product slug url for this item (provided for extensibility)
        """
        return "{0}".format(self.site_logo)

    # From http://ishcray.com/downloading-and-saving-image-to-imagefield-in-django 
    def save(self, url="", *args, **kwargs):
        if self.site_logo != '' and url != '':
            image = download_image(url)
            try:
                filename = urlparse.urlparse(url).path.split('/')[-1]
                self.site_logo = filename
                tempfile = image 
                tempfile_io = cStringIO.StringIO()
                tempfile.save(tempfile_io, format=image.format)
                self.site_logo.save(filename, ContentFile(tempfile_io.getvalue()), save=False )
            except Exception, e:
                print("Error trying to save model: saving image failed: " + str(e))
                pass
        super(Website, self).save(*args, **kwargs)


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


