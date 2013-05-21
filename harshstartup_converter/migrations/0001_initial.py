# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rule'
        db.create_table(u'harshstartup_converter_rule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['harshstartup_converter.Rule'])),
            ('pattern', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('replacement', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'harshstartup_converter', ['Rule'])

        # Adding model 'Test'
        db.create_table(u'harshstartup_converter_test', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['harshstartup_converter.Rule'], null=True, blank=True)),
            ('input', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('output', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal(u'harshstartup_converter', ['Test'])


    def backwards(self, orm):
        # Deleting model 'Rule'
        db.delete_table(u'harshstartup_converter_rule')

        # Deleting model 'Test'
        db.delete_table(u'harshstartup_converter_test')


    models = {
        u'harshstartup_converter.rule': {
            'Meta': {'object_name': 'Rule'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
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