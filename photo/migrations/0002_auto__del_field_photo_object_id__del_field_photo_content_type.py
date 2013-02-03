# flake8: noqa
# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Photo.object_id'
        db.delete_column('photo_photo', 'object_id')

        # Deleting field 'Photo.content_type'
        db.delete_column('photo_photo', 'content_type_id')


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Photo.object_id'
        raise RuntimeError("Cannot reverse this migration. 'Photo.object_id' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Photo.content_type'
        raise RuntimeError("Cannot reverse this migration. 'Photo.content_type' and its values cannot be restored.")


    models = {
        'photo.photo': {
            'Meta': {'object_name': 'Photo'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'caption': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageWithThumbnailsField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'source_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['photo']
