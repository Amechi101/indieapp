# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ProductCategoryMain'
        db.delete_table(u'product_extend_productcategorymain')

        # Deleting model 'Designer'
        db.delete_table(u'product_extend_designer')

        # Deleting model 'ProductCategorySub'
        db.delete_table(u'product_extend_productcategorysub')

        # Deleting field 'ProductExtend.designer'
        db.delete_column(u'product_extend_productextend', 'designer_id')

        # Deleting field 'ProductExtend.category_main'
        db.delete_column(u'product_extend_productextend', 'category_main_id')

        # Deleting field 'ProductExtend.category_sub'
        db.delete_column(u'product_extend_productextend', 'category_sub_id')

        # Adding field 'ProductExtend.label_name'
        db.add_column(u'product_extend_productextend', 'label_name',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ProductExtend.product_website_name'
        db.add_column(u'product_extend_productextend', 'product_website_name',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'ProductCategoryMain'
        db.create_table(u'product_extend_productcategorymain', (
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L, null=True, blank=True)),
        ))
        db.send_create_signal(u'product_extend', ['ProductCategoryMain'])

        # Adding model 'Designer'
        db.create_table(u'product_extend_designer', (
            ('label_name', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
        ))
        db.send_create_signal(u'product_extend', ['Designer'])

        # Adding model 'ProductCategorySub'
        db.create_table(u'product_extend_productcategorysub', (
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L, null=True, blank=True)),
        ))
        db.send_create_signal(u'product_extend', ['ProductCategorySub'])


        # User chose to not deal with backwards NULL issues for 'ProductExtend.designer'
        raise RuntimeError("Cannot reverse this migration. 'ProductExtend.designer' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ProductExtend.designer'
        db.add_column(u'product_extend_productextend', 'designer',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product_extend.Designer']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ProductExtend.category_main'
        raise RuntimeError("Cannot reverse this migration. 'ProductExtend.category_main' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ProductExtend.category_main'
        db.add_column(u'product_extend_productextend', 'category_main',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product_extend.ProductCategoryMain']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ProductExtend.category_sub'
        raise RuntimeError("Cannot reverse this migration. 'ProductExtend.category_sub' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ProductExtend.category_sub'
        db.add_column(u'product_extend_productextend', 'category_sub',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product_extend.ProductCategorySub']),
                      keep_default=False)

        # Deleting field 'ProductExtend.label_name'
        db.delete_column(u'product_extend_productextend', 'label_name')

        # Deleting field 'ProductExtend.product_website_name'
        db.delete_column(u'product_extend_productextend', 'product_website_name')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'product_extend.productextend': {
            'Meta': {'object_name': 'ProductExtend', '_ormbases': ['shop.Product']},
            'label_name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'product_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shop.Product']", 'unique': 'True', 'primary_key': 'True'}),
            'product_website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'product_website_name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
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