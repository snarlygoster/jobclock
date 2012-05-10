# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'WorkPeriod'
        db.create_table('timeclock_workperiod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_punch', self.gf('django.db.models.fields.related.ForeignKey')(related_name='workperiod_start_punch', unique=True, to=orm['timeclock.ClockPunch'])),
            ('end_punch', self.gf('django.db.models.fields.related.ForeignKey')(related_name='workperiod_end_punch', to=orm['timeclock.ClockPunch'])),
        ))
        db.send_create_signal('timeclock', ['WorkPeriod'])

        # Adding field 'ClockPunch.logged'
        db.add_column('timeclock_clockpunch', 'logged', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'WorkPeriod'
        db.delete_table('timeclock_workperiod')

        # Deleting field 'ClockPunch.logged'
        db.delete_column('timeclock_clockpunch', 'logged')


    models = {
        'timeclock.activity': {
            'Meta': {'ordering': "['ticket']", 'object_name': 'Activity'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'on_work_queue': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ticket': ('django.db.models.fields.CharField', [], {'default': "'2012-05-0001'", 'unique': 'True', 'max_length': '40'})
        },
        'timeclock.clockpunch': {
            'Meta': {'ordering': "['-timestamp']", 'object_name': 'ClockPunch'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timeclock.Activity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timeclock.Worker']"})
        },
        'timeclock.worker': {
            'Meta': {'ordering': "['name']", 'object_name': 'Worker'},
            'can_work': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'timeclock.workperiod': {
            'Meta': {'object_name': 'WorkPeriod'},
            'end_punch': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'workperiod_end_punch'", 'to': "orm['timeclock.ClockPunch']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_punch': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'workperiod_start_punch'", 'unique': 'True', 'to': "orm['timeclock.ClockPunch']"})
        }
    }

    complete_apps = ['timeclock']
