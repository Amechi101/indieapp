# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Website.product_image_feature'
        db.add_column(u'_backend_api_website', 'product_image_feature',
                      self.gf('cloudinary.models.CloudinaryField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Website.product_image_feature'
        db.delete_column(u'_backend_api_website', 'product_image_feature')


    models = {
        u'_backend_api.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'product_category': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'product_image': ('cloudinary.models.CloudinaryField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'product_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'}),
            'product_slug_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'product_website_name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['_backend_api.Website']", 'null': 'True'})
        },
        u'_backend_api.website': {
            'Meta': {'object_name': 'Website'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'menswear': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'product_image_feature': ('cloudinary.models.CloudinaryField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_logo_image': ('cloudinary.models.CloudinaryField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'website_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'womenswear': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['_backend_api']