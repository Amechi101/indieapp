# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Brand'
        db.create_table(u'_backend_api_brand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brand_name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True, blank=True)),
            ('brand_founded', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True)),
            ('brand_origin_city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('brand_origin_state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('brand_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('brand_product_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True, null=True, blank=True)),
            ('brand_logo', self.gf('cloudinary.models.CloudinaryField')(max_length=100, null=True, blank=True)),
            ('brand_feature_image', self.gf('cloudinary.models.CloudinaryField')(max_length=100, null=True, blank=True)),
            ('brand_website_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('brand_email', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('brand_state', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brand_location_state', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brand_email_state', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('menswear', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('womenswear', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'_backend_api', ['Brand'])

        # Adding model 'Product'
        db.create_table(u'_backend_api_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('product_price', self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=30, decimal_places=2)),
            ('product_image', self.gf('cloudinary.models.CloudinaryField')(max_length=255, null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['_backend_api.Brand'], null=True)),
        ))
        db.send_create_signal(u'_backend_api', ['Product'])

        # Adding model 'Location'
        db.create_table(u'_backend_api_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brand_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('brand_city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('brand_state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['_backend_api.Brand'], null=True)),
        ))
        db.send_create_signal(u'_backend_api', ['Location'])


    def backwards(self, orm):
        # Deleting model 'Brand'
        db.delete_table(u'_backend_api_brand')

        # Deleting model 'Product'
        db.delete_table(u'_backend_api_product')

        # Deleting model 'Location'
        db.delete_table(u'_backend_api_location')


    models = {
        u'_backend_api.brand': {
            'Meta': {'object_name': 'Brand'},
            'brand_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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