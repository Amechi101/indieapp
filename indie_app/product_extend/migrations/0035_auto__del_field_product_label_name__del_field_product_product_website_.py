# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Product.label_name'
        db.delete_column(u'product_extend_product', 'label_name')

        # Deleting field 'Product.product_website'
        db.delete_column(u'product_extend_product', 'product_website')

        # Deleting field 'Product.unit_price'
        db.delete_column(u'product_extend_product', 'unit_price')

        # Deleting field 'Product.product_category_main'
        db.delete_column(u'product_extend_product', 'product_category_main')

        # Adding field 'Product.product_price'
        db.add_column(u'product_extend_product', 'product_price',
                      self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=30, decimal_places=2),
                      keep_default=False)

        # Adding field 'Product.product_category'
        db.add_column(u'product_extend_product', 'product_category',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.product_website_url'
        db.add_column(u'product_extend_product', 'product_website_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Product.name'
        db.alter_column(u'product_extend_product', 'name', self.gf('django.db.models.fields.CharField')(max_length=254, null=True))

    def backwards(self, orm):
        # Adding field 'Product.label_name'
        db.add_column(u'product_extend_product', 'label_name',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.product_website'
        db.add_column(u'product_extend_product', 'product_website',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.unit_price'
        db.add_column(u'product_extend_product', 'unit_price',
                      self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=30, decimal_places=2),
                      keep_default=False)

        # Adding field 'Product.product_category_main'
        db.add_column(u'product_extend_product', 'product_category_main',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Product.product_price'
        db.delete_column(u'product_extend_product', 'product_price')

        # Deleting field 'Product.product_category'
        db.delete_column(u'product_extend_product', 'product_category')

        # Deleting field 'Product.product_website_url'
        db.delete_column(u'product_extend_product', 'product_website_url')


        # Changing field 'Product.name'
        db.alter_column(u'product_extend_product', 'name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    models = {
        u'product_extend.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'product_category': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'product_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'product_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'}),
            'product_slug_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'product_website_name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'product_website_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['product_extend']