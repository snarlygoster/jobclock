# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'JobDetails'
        db.create_table('timeclock_jobdetails', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('timeclock', ['JobDetails'])

        # Adding model 'Customer'
        db.create_table('timeclock_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('telephone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20)),
        ))
        db.send_create_signal('timeclock', ['Customer'])

        # Adding model 'WorkOrder'
        db.create_table('timeclock_workorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('initiation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('ticket', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeclock.Activity'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeclock.Customer'])),
            ('details', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeclock.JobDetails'])),
        ))
        db.send_create_signal('timeclock', ['WorkOrder'])


    def backwards(self, orm):
        
        # Deleting model 'JobDetails'
        db.delete_table('timeclock_jobdetails')

        # Deleting model 'Customer'
        db.delete_table('timeclock_customer')

        # Deleting model 'WorkOrder'
        db.delete_table('timeclock_workorder')


    models = {
        'timeclock.activity': {
            'Meta': {'ordering': "['ticket']", 'object_name': 'Activity'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'on_work_queue': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ticket': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
        },
        'timeclock.clockpunch': {
            'Meta': {'ordering': "['-timestamp']", 'object_name': 'ClockPunch'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timeclock.Activity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timeclock.Worker']"})
        },
        'timeclock.customer': {
            'Meta': {'ordering': "['name']", 'object_name': 'Customer'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telephone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'})
        },
        'timeclock.jobdetails': {
            'Meta': {'ordering': "['type']", 'object_name': 'JobDetails'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'timeclock.worker': {
            'Meta': {'ordering': "['name']", 'object_name': 'Worker'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'timeclock.workorder': {
            'Meta': {'ordering': "['initiation_date']", 'object_name': 'WorkOrder'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timeclock.Customer']"}),
            'details': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timeclock.JobDetails']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'ticket': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timeclock.Activity']"})
        }
    }

    complete_apps = ['timeclock']
