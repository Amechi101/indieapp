# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Website.description'
        db.add_column(u'website_website', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Website.website_slug'
        db.add_column(u'website_website', 'website_slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Website.site_logo'
        db.add_column(u'website_website', 'site_logo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Website.menswear'
        db.add_column(u'website_website', 'menswear',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Website.womenswear'
        db.add_column(u'website_website', 'womenswear',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Website.active'
        db.add_column(u'website_website', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Website.date_added'
        db.add_column(u'website_website', 'date_added',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Website.last_modified'
        db.add_column(u'website_website', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Website.description'
        db.delete_column(u'website_website', 'description')

        # Deleting field 'Website.website_slug'
        db.delete_column(u'website_website', 'website_slug')

        # Deleting field 'Website.site_logo'
        db.delete_column(u'website_website', 'site_logo')

        # Deleting field 'Website.menswear'
        db.delete_column(u'website_website', 'menswear')

        # Deleting field 'Website.womenswear'
        db.delete_column(u'website_website', 'womenswear')

        # Deleting field 'Website.active'
        db.delete_column(u'website_website', 'active')

        # Deleting field 'Website.date_added'
        db.delete_column(u'website_website', 'date_added')

        # Deleting field 'Website.last_modified'
        db.delete_column(u'website_website', 'last_modified')


    models = {
        u'website.website': {
            'Meta': {'object_name': 'Website'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'menswear': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'site_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'website_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'womenswear': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['website']