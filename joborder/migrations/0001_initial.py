# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Product'
        db.create_table('joborder_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('joborder', ['Product'])

        # Adding model 'Customer'
        db.create_table('joborder_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('joborder', ['Customer'])

        # Adding model 'JobOrder'
        db.create_table('joborder_joborder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['joborder.Product'])),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('duedate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('covermaterial', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('joborder', ['JobOrder'])

        # Adding model 'ScheduledJob'
        db.create_table('joborder_scheduledjob', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('joborder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['joborder.JobOrder'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['joborder.Customer'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal('joborder', ['ScheduledJob'])


    def backwards(self, orm):
        
        # Deleting model 'Product'
        db.delete_table('joborder_product')

        # Deleting model 'Customer'
        db.delete_table('joborder_customer')

        # Deleting model 'JobOrder'
        db.delete_table('joborder_joborder')

        # Deleting model 'ScheduledJob'
        db.delete_table('joborder_scheduledjob')


    models = {
        'joborder.customer': {
            'Meta': {'ordering': "['name']", 'object_name': 'Customer'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'joborder.joborder': {
            'Meta': {'object_name': 'JobOrder'},
            'covermaterial': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'duedate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['joborder.Product']"}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'joborder.product': {
            'Meta': {'ordering': "['name']", 'object_name': 'Product'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'joborder.scheduledjob': {
            'Meta': {'ordering': "['creation_date']", 'object_name': 'ScheduledJob'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['joborder.Customer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joborder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['joborder.JobOrder']"})
        }
    }

    complete_apps = ['joborder']
