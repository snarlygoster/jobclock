# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'WorkOrderItem.work_order'
        db.add_column('workorder_workorderitem', 'work_order', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['workorder.WorkOrder']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'WorkOrderItem.work_order'
        db.delete_column('workorder_workorderitem', 'work_order_id')


    models = {
        'timeclock.activity': {
            'Meta': {'ordering': "['ticket']", 'object_name': 'Activity'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'on_work_queue': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ticket': ('django.db.models.fields.CharField', [], {'default': "'2012-06-0003'", 'unique': 'True', 'max_length': '40'})
        },
        'workorder.customer': {
            'Meta': {'ordering': "['name']", 'object_name': 'Customer'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telephone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'})
        },
        'workorder.workorder': {
            'Meta': {'ordering': "['creation_date']", 'object_name': 'WorkOrder'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workorder.Customer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ticket': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['timeclock.Activity']", 'unique': 'True'})
        },
        'workorder.workorderitem': {
            'Meta': {'ordering': "['number']", 'object_name': 'WorkOrderItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'work_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workorder.WorkOrder']"})
        }
    }

    complete_apps = ['workorder']
