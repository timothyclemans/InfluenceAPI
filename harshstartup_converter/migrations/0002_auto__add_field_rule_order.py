# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Rule.order'
        db.add_column(u'harshstartup_converter_rule', 'order',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Rule.order'
        db.delete_column(u'harshstartup_converter_rule', 'order')


    models = {
        u'harshstartup_converter.rule': {
            'Meta': {'object_name': 'Rule'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['harshstartup_converter.Rule']"}),
            'pattern': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'replacement': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'harshstartup_converter.test': {
            'Meta': {'object_name': 'Test'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'input': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'output': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'rule': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['harshstartup_converter.Rule']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['harshstartup_converter']