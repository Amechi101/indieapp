# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Product.website'
        db.delete_column(u'product_extend_product', 'website_id')

        # Deleting field 'Product.active'
        db.delete_column(u'product_extend_product', 'active')

        # Deleting field 'Product.label_name'
        db.delete_column(u'product_extend_product', 'label_name')

        # Deleting field 'Product.last_modified'
        db.delete_column(u'product_extend_product', 'last_modified')

        # Deleting field 'Product.product_slug_url'
        db.delete_column(u'product_extend_product', 'product_slug_url')

        # Deleting field 'Product.product_website'
        db.delete_column(u'product_extend_product', 'product_website')

        # Deleting field 'Product.date_added'
        db.delete_column(u'product_extend_product', 'date_added')

        # Deleting field 'Product.product_img'
        db.delete_column(u'product_extend_product', 'product_img')

        # Deleting field 'Product.name'
        db.delete_column(u'product_extend_product', 'name')

        # Deleting field 'Product.unit_price'
        db.delete_column(u'product_extend_product', 'unit_price')

        # Deleting field 'Product.product_category_main'
        db.delete_column(u'product_extend_product', 'product_category_main')

        # Deleting field 'Product.product_website_name'
        db.delete_column(u'product_extend_product', 'product_website_name')


    def backwards(self, orm):
        # Adding field 'Product.website'
        db.add_column(u'product_extend_product', 'website',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Website'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.active'
        db.add_column(u'product_extend_product', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Product.label_name'
        db.add_column(u'product_extend_product', 'label_name',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Product.last_modified'
        raise RuntimeError("Cannot reverse this migration. 'Product.last_modified' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Product.last_modified'
        db.add_column(u'product_extend_product', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.product_slug_url'
        db.add_column(u'product_extend_product', 'product_slug_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.product_website'
        db.add_column(u'product_extend_product', 'product_website',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Product.date_added'
        raise RuntimeError("Cannot reverse this migration. 'Product.date_added' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Product.date_added'
        db.add_column(u'product_extend_product', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.product_img'
        db.add_column(u'product_extend_product', 'product_img',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Product.name'
        raise RuntimeError("Cannot reverse this migration. 'Product.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Product.name'
        db.add_column(u'product_extend_product', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)

        # Adding field 'Product.unit_price'
        db.add_column(u'product_extend_product', 'unit_price',
                      self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=30, decimal_places=2),
                      keep_default=False)

        # Adding field 'Product.product_category_main'
        db.add_column(u'product_extend_product', 'product_category_main',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.product_website_name'
        db.add_column(u'product_extend_product', 'product_website_name',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)


    models = {
        u'product_extend.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['product_extend']