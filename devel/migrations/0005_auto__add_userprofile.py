# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ('main', '0059_auto__del_userprofile'),
    )

    def forwards(self, orm):
        if not db.dry_run:
            db.send_create_signal('devel', ['UserProfile'])
            orm['contenttypes.ContentType'].objects.filter(
                    app_label='main', model='userprofile').update(
                    app_label='devel')

    def backwards(self, orm):
        pass

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'devel.masterkey': {
            'Meta': {'ordering': "('created',)", 'object_name': 'MasterKey'},
            'created': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'masterkey_owner'", 'to': "orm['auth.User']"}),
            'pgp_key': ('devel.fields.PGPKeyField', [], {'max_length': '40'}),
            'revoked': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'revoker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'masterkey_revoker'", 'to': "orm['auth.User']"})
        },
        'devel.pgpsignature': {
            'Meta': {'object_name': 'PGPSignature'},
            'created': ('django.db.models.fields.DateField', [], {}),
            'expires': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signee': ('devel.fields.PGPKeyField', [], {'max_length': '40'}),
            'signer': ('devel.fields.PGPKeyField', [], {'max_length': '40'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'devel.userprofile': {
            'Meta': {'object_name': 'UserProfile', 'db_table': "'user_profiles'"},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'allowed_repos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Repo']", 'symmetrical': 'False', 'blank': 'True'}),
            'favorite_distros': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'latin_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'notify': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'other_contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pgp_key': ('devel.fields.PGPKeyField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.FileField', [], {'default': "'devs/silhouette.png'", 'max_length': '100'}),
            'public_email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'roles': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_zone': ('django.db.models.fields.CharField', [], {'default': "'UTC'", 'max_length': '100'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'userprofile'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'yob': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'main.repo': {
            'Meta': {'ordering': "['name']", 'object_name': 'Repo', 'db_table': "'repos'"},
            'bugs_category': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            'bugs_project': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'staging': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'svn_root': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'testing': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['devel']
