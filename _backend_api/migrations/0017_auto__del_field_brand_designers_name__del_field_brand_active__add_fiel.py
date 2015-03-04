# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Brand.designers_name'
        db.delete_column(u'_backend_api_brand', 'designers_name')

        # Deleting field 'Brand.active'
        db.delete_column(u'_backend_api_brand', 'active')

        # Adding field 'Brand.brand_website_url'
        db.add_column(u'_backend_api_brand', 'brand_website_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Brand.brand_email'
        db.add_column(u'_backend_api_brand', 'brand_email',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Brand.brand_state'
        db.add_column(u'_backend_api_brand', 'brand_state',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Brand.brand_location_state'
        db.add_column(u'_backend_api_brand', 'brand_location_state',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Brand.brand_email_state'
        db.add_column(u'_backend_api_brand', 'brand_email_state',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Location.brand_website_url'
        db.delete_column(u'_backend_api_location', 'brand_website_url')

        # Deleting field 'Location.contact_type'
        db.delete_column(u'_backend_api_location', 'contact_type')

        # Deleting field 'Location.brand_website_name'
        db.delete_column(u'_backend_api_location', 'brand_website_name')

        # Deleting field 'Location.brand_email_state'
        db.delete_column(u'_backend_api_location', 'brand_email_state')

        # Deleting field 'Location.brand_email'
        db.delete_column(u'_backend_api_location', 'brand_email')

        # Deleting field 'Product.active'
        db.delete_column(u'_backend_api_product', 'active')


    def backwards(self, orm):
        # Adding field 'Brand.designers_name'
        db.add_column(u'_backend_api_brand', 'designers_name',
                      self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Brand.active'
        db.add_column(u'_backend_api_brand', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'Brand.brand_website_url'
        db.delete_column(u'_backend_api_brand', 'brand_website_url')

        # Deleting field 'Brand.brand_email'
        db.delete_column(u'_backend_api_brand', 'brand_email')

        # Deleting field 'Brand.brand_state'
        db.delete_column(u'_backend_api_brand', 'brand_state')

        # Deleting field 'Brand.brand_location_state'
        db.delete_column(u'_backend_api_brand', 'brand_location_state')

        # Deleting field 'Brand.brand_email_state'
        db.delete_column(u'_backend_api_brand', 'brand_email_state')

        # Adding field 'Location.brand_website_url'
        db.add_column(u'_backend_api_location', 'brand_website_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Location.contact_type'
        db.add_column(u'_backend_api_location', 'contact_type',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Location.brand_website_name'
        db.add_column(u'_backend_api_location', 'brand_website_name',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Location.brand_email_state'
        db.add_column(u'_backend_api_location', 'brand_email_state',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Location.brand_email'
        db.add_column(u'_backend_api_location', 'brand_email',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.active'
        db.add_column(u'_backend_api_product', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    models = {
        u'_backend_api.brand': {
            'Meta': {'object_name': 'Brand'},
            'brand_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'brand_detail_slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'brand_email': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'brand_email_state': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brand_feature_image': ('cloudinary.models.CloudinaryField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'brand_founded': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True'}),
            'brand_location_state': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brand_logo': ('cloudinary.models.CloudinaryField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'brand_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'brand_origin_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'brand_origin_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'brand_product_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'brand_state': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brand_website_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'menswear': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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