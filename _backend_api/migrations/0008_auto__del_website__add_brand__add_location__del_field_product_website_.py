# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Website'
        db.delete_table(u'_backend_api_website')

        # Adding model 'Brand'
        db.create_table(u'_backend_api_brand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('designers_name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True, blank=True)),
            ('brand_name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True, blank=True)),
            ('brand_founded', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True)),
            ('brand_origin_city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('brand_origin_state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('brand_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('brand_product_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('brand_detail_slug', self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True, null=True, blank=True)),
            ('brand_logo', self.gf('cloudinary.models.CloudinaryField')(max_length=100, null=True, blank=True)),
            ('brand_feature_image', self.gf('cloudinary.models.CloudinaryField')(max_length=100, null=True, blank=True)),
            ('menswear', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('womenswear', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'_backend_api', ['Brand'])

        # Adding model 'Location'
        db.create_table(u'_backend_api_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_type', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True, blank=True)),
            ('brand_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('brand_city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('brand_state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('brand_website_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('brand_website_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('brand_email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('brand_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['_backend_api.Brand'], null=True)),
        ))
        db.send_create_signal(u'_backend_api', ['Location'])

        # Deleting field 'Product.website'
        db.delete_column(u'_backend_api_product', 'website_id')

        # Deleting field 'Product.product_category'
        db.delete_column(u'_backend_api_product', 'product_category')

        # Deleting field 'Product.product_slug_url'
        db.delete_column(u'_backend_api_product', 'product_slug_url')

        # Deleting field 'Product.product_website_name'
        db.delete_column(u'_backend_api_product', 'product_website_name')

        # Adding field 'Product.brand_product'
        db.add_column(u'_backend_api_product', 'brand_product',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['_backend_api.Brand'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Website'
        db.create_table(u'_backend_api_website', (
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('product_image_feature', self.gf('cloudinary.models.CloudinaryField')(max_length=100, null=True, blank=True)),
            ('womenswear', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site_logo_image', self.gf('cloudinary.models.CloudinaryField')(max_length=100, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, null=True, blank=True)),
            ('menswear', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('website_slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'_backend_api', ['Website'])

        # Deleting model 'Brand'
        db.delete_table(u'_backend_api_brand')

        # Deleting model 'Location'
        db.delete_table(u'_backend_api_location')

        # Adding field 'Product.website'
        db.add_column(u'_backend_api_product', 'website',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['_backend_api.Website'], null=True),
                      keep_default=False)

        # Adding field 'Product.product_category'
        db.add_column(u'_backend_api_product', 'product_category',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.product_slug_url'
        db.add_column(u'_backend_api_product', 'product_slug_url',
                      self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.product_website_name'
        db.add_column(u'_backend_api_product', 'product_website_name',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Product.brand_product'
        db.delete_column(u'_backend_api_product', 'brand_product_id')


    models = {
        u'_backend_api.brand': {
            'Meta': {'object_name': 'Brand'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'brand_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'brand_detail_slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'brand_feature_image': ('cloudinary.models.CloudinaryField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'brand_founded': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True'}),
            'brand_logo': ('cloudinary.models.CloudinaryField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'brand_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'brand_origin_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'brand_origin_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'brand_product_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'designers_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'menswear': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'womenswear': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'_backend_api.location': {
            'Meta': {'object_name': 'Location'},
            'brand_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'brand_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'brand_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'brand_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['_backend_api.Brand']", 'null': 'True'}),
            'brand_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'brand_website_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'brand_website_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'contact_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'_backend_api.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'brand_product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['_backend_api.Brand']", 'null': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'product_image': ('cloudinary.models.CloudinaryField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'})
        }
    }

    complete_apps = ['_backend_api']