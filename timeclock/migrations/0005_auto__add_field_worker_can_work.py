# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Worker.can_work'
        db.add_column('timeclock_worker', 'can_work', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Worker.can_work'
        db.delete_column('timeclock_worker', 'can_work')


    models = {
        'timeclock.activity': {
            'Meta': {'ordering': "['ticket']", 'object_name': 'Activity'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'on_work_queue': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ticket': ('django.db.models.fields.CharField', [], {'default': "'2012-03-0005'", 'unique': 'True', 'max_length': '40'})
        },
        'timeclock.clockpunch': {
            'Meta': {'ordering': "['-timestamp']", 'object_name': 'ClockPunch'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timeclock.Activity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timeclock.Worker']"})
        },
        'timeclock.worker': {
            'Meta': {'ordering': "['name']", 'object_name': 'Worker'},
            'can_work': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['timeclock']
