# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Product.detail_spec'
        db.alter_column('joborder_product', 'detail_spec', self.gf('picklefield.fields.PickledObjectField')())

        # Changing field 'JobItem.detail_answers'
        db.alter_column('joborder_jobitem', 'detail_answers', self.gf('picklefield.fields.PickledObjectField')())


    def backwards(self, orm):
        
        # Changing field 'Product.detail_spec'
        db.alter_column('joborder_product', 'detail_spec', self.gf('django.db.models.fields.CharField')(max_length=1000))

        # Changing field 'JobItem.detail_answers'
        db.alter_column('joborder_jobitem', 'detail_answers', self.gf('django.db.models.fields.CharField')(max_length=1000))


    models = {
        'joborder.jobitem': {
            'Meta': {'object_name': 'JobItem'},
            'detail_answers': ('picklefield.fields.PickledObjectField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['joborder.Product']"}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'joborder.product': {
            'Meta': {'ordering': "['name']", 'object_name': 'Product'},
            'detail_spec': ('picklefield.fields.PickledObjectField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['joborder']
