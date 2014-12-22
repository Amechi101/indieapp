# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Website'
        db.create_table(u'website_website', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'website', ['Website'])


    def backwards(self, orm):
        # Deleting model 'Website'
        db.delete_table(u'website_website')


    models = {
        u'website.website': {
            'Meta': {'object_name': 'Website'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['website']