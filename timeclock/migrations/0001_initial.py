# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Worker'
        db.create_table('timeclock_worker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('timeclock', ['Worker'])

        # Adding model 'Activity'
        db.create_table('timeclock_activity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ticket', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('job_complete', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('timeclock', ['Activity'])

        # Adding model 'ClockPunch'
        db.create_table('timeclock_clockpunch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeclock.Activity'])),
            ('worker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeclock.Worker'])),
        ))
        db.send_create_signal('timeclock', ['ClockPunch'])


    def backwards(self, orm):
        
        # Deleting model 'Worker'
        db.delete_table('timeclock_worker')

        # Deleting model 'Activity'
        db.delete_table('timeclock_activity')

        # Deleting model 'ClockPunch'
        db.delete_table('timeclock_clockpunch')


    models = {
        'timeclock.activity': {
            'Meta': {'ordering': "['ticket']", 'object_name': 'Activity'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ticket': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['timeclock']
