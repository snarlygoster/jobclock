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
            ('detail_spec', self.gf('django.db.models.fields.CharField')(default='Cover Material', max_length=1000)),
        ))
        db.send_create_signal('joborder', ['Product'])

        # Adding model 'JobItem'
        db.create_table('joborder_jobitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['joborder.Product'])),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('detail_answers', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('joborder', ['JobItem'])


    def backwards(self, orm):
        
        # Deleting model 'Product'
        db.delete_table('joborder_product')

        # Deleting model 'JobItem'
        db.delete_table('joborder_jobitem')


    models = {
        'joborder.jobitem': {
            'Meta': {'object_name': 'JobItem'},
            'detail_answers': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['joborder.Product']"}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'joborder.product': {
            'Meta': {'ordering': "['name']", 'object_name': 'Product'},
            'detail_spec': ('django.db.models.fields.CharField', [], {'default': "'Cover Material'", 'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['joborder']