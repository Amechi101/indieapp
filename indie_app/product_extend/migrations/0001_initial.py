# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Designer'
        db.create_table(u'product_extend_designer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('label_name', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'product_extend', ['Designer'])

        # Adding model 'ProductCategoryMain'
        db.create_table(u'product_extend_productcategorymain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'product_extend', ['ProductCategoryMain'])

        # Adding model 'ProductCategorySub'
        db.create_table(u'product_extend_productcategorysub', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'product_extend', ['ProductCategorySub'])

        # Adding model 'ProductExtend'
        db.create_table(u'product_extend_productextend', (
            (u'product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['shop.Product'], unique=True, primary_key=True)),
            ('product_website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('product_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('designer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product_extend.Designer'])),
            ('category_main', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product_extend.ProductCategoryMain'])),
            ('category_sub', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product_extend.ProductCategorySub'])),
        ))
        db.send_create_signal(u'product_extend', ['ProductExtend'])


    def backwards(self, orm):
        # Deleting model 'Designer'
        db.delete_table(u'product_extend_designer')

        # Deleting model 'ProductCategoryMain'
        db.delete_table(u'product_extend_productcategorymain')

        # Deleting model 'ProductCategorySub'
        db.delete_table(u'product_extend_productcategorysub')

        # Deleting model 'ProductExtend'
        db.delete_table(u'product_extend_productextend')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'product_extend.designer': {
            'Meta': {'object_name': 'Designer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'label_name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        u'product_extend.productcategorymain': {
            'Meta': {'object_name': 'ProductCategoryMain'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'product_extend.productcategorysub': {
            'Meta': {'object_name': 'ProductCategorySub'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'product_extend.productextend': {
            'Meta': {'object_name': 'ProductExtend', '_ormbases': ['shop.Product']},
            'category_main': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product_extend.ProductCategoryMain']"}),
            'category_sub': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product_extend.ProductCategorySub']"}),
            'designer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product_extend.Designer']"}),
            'product_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shop.Product']", 'unique': 'True', 'primary_key': 'True'}),
            'product_website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_shop.product_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'})
        }
    }

    complete_apps = ['product_extend']