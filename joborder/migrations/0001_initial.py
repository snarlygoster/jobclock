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

        # Adding model 'JobOrder'
        db.create_table('joborder_joborder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['joborder.Product'])),
        ))
        db.send_create_signal('joborder', ['JobOrder'])


    def backwards(self, orm):
        
        # Deleting model 'Product'
        db.delete_table('joborder_product')

        # Deleting model 'JobOrder'
        db.delete_table('joborder_joborder')


    models = {
        'joborder.joborder': {
            'Meta': {'object_name': 'JobOrder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['joborder.Product']"})
        },
        'joborder.product': {
            'Meta': {'ordering': "['name']", 'object_name': 'Product'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['joborder']
