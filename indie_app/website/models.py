from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext_lazy as _

import datetime


class Website(models.Model):
    name = models.CharField(max_length=254, blank=True, null=True, unique=True)
    description = models.TextField(null=True, blank=True)
    website_slug = models.SlugField(verbose_name=_('Website Slug'), unique=True,  null=True,  blank=True)
    
    # Points to a Cloudinary image
    site_logo_image = CloudinaryField('image', null=True, blank=True)
    
    menswear = models.BooleanField(default=False, verbose_name=_('Menswear'))
    womenswear = models.BooleanField(default=False, verbose_name=_('Womenswear'))
    
    active = models.BooleanField(default=True, verbose_name=_('Active'))

    #For Admin Purposes and filtering, to keep track of new and old  in the database by administrative users
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('Date added'))
    last_modified = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Last modified') )

    #Metadata
    class Meta: 
        verbose_name = _('Website')
        verbose_name_plural = _('Websites')

    def __unicode__(self):
        return "{0}".format(self.name)

    def __unicode__(self):
        try:
            public_id = self.site_logo_image.public_id
        except AttributeError:
            public_id = ''
        return "Website Image {0}:{1}>".format(self.name, public_id)

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


