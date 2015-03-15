# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Brand.brand_product_description'
        db.delete_column(u'_backend_api_brand', 'brand_product_description')

        # Deleting field 'Brand.brand_description'
        db.delete_column(u'_backend_api_brand', 'brand_description')

        # Adding field 'Brand.brand_about_description'
        db.add_column(u'_backend_api_brand', 'brand_about_description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Brand.brand_collection_description'
        db.add_column(u'_backend_api_brand', 'brand_collection_description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Brand.brand_about_image'
        db.add_column(u'_backend_api_brand', 'brand_about_image',
                      self.gf('cloudinary.models.CloudinaryField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Brand.brand_collection_image'
        db.add_column(u'_backend_api_brand', 'brand_collection_image',
                      self.gf('cloudinary.models.CloudinaryField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Brand.brand_connect_image'
        db.add_column(u'_backend_api_brand', 'brand_connect_image',
                      self.gf('cloudinary.models.CloudinaryField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Brand.brand_website_state'
        db.add_column(u'_backend_api_brand', 'brand_website_state',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Brand.brand_email'
        db.alter_column(u'_backend_api_brand', 'brand_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True))

    def backwards(self, orm):
        # Adding field 'Brand.brand_product_description'
        db.add_column(u'_backend_api_brand', 'brand_product_description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Brand.brand_description'
        db.add_column(u'_backend_api_brand', 'brand_description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Brand.brand_about_description'
        db.delete_column(u'_backend_api_brand', 'brand_about_description')

        # Deleting field 'Brand.brand_collection_description'
        db.delete_column(u'_backend_api_brand', 'brand_collection_description')

        # Deleting field 'Brand.brand_about_image'
        db.delete_column(u'_backend_api_brand', 'brand_about_image')

        # Deleting field 'Brand.brand_collection_image'
        db.delete_column(u'_backend_api_brand', 'brand_collection_image')

        # Deleting field 'Brand.brand_connect_image'
        db.delete_column(u'_backend_api_brand', 'brand_connect_image')

        # Deleting field 'Brand.brand_website_state'
        db.delete_column(u'_backend_api_brand', 'brand_website_state')


        # Changing field 'Brand.brand_email'
        db.alter_column(u'_backend_api_brand', 'brand_email', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    models = {
        u'_backend_api.brand': {
            'Meta': {'object_name': 'Brand'},
            'brand_about_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'brand_about_image': ('cloudinary.models.CloudinaryField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'brand_collection_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'brand_collection_image': ('cloudinary.models.CloudinaryField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'brand_connect_image': ('cloudinary.models.CloudinaryField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'brand_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'brand_email_state': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brand_feature_image': ('cloudinary.models.CloudinaryField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'brand_founded': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True'}),
            'brand_location_state': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brand_logo': ('cloudinary.models.CloudinaryField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'brand_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'brand_origin_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'brand_origin_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'brand_state': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brand_website_state': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brand_website_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'menswear': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'womenswear': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'_backend_api.location': {
            'Meta': {'object_name': 'Location'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['_backend_api.Brand']", 'null': 'True'}),
            'brand_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'brand_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'brand_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'_backend_api.product': {
            'Meta': {'object_name': 'Product'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['_backend_api.Brand']", 'null': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'product_image': ('cloudinary.models.CloudinaryField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'})
        }
    }

    complete_apps = ['_backend_api']