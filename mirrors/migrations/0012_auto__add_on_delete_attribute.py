# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.alter_column('mirrors_mirror', 'upstream_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mirrors.Mirror'], null=True, on_delete=models.SET_NULL))
        db.alter_column('mirrors_mirrorurl', 'protocol_id', self.gf('django.db.models.fields.related.ForeignKey')(on_delete=models.PROTECT, to=orm['mirrors.MirrorProtocol']))

    def backwards(self, orm):
        db.alter_column('mirrors_mirror', 'upstream_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mirrors.Mirror'], null=True))
        db.alter_column('mirrors_mirrorurl', 'protocol_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mirrors.MirrorProtocol']))

    models = {
        'mirrors.mirror': {
            'Meta': {'ordering': "('country', 'name')", 'object_name': 'Mirror'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'admin_email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isos': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rsync_password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'rsync_user': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'tier': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            'upstream': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mirrors.Mirror']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        },
        'mirrors.mirrorlog': {
            'Meta': {'object_name': 'MirrorLog'},
            'check_time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'duration': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'error': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_success': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_sync': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'logs'", 'to': "orm['mirrors.MirrorUrl']"})
        },
        'mirrors.mirrorprotocol': {
            'Meta': {'ordering': "('protocol',)", 'object_name': 'MirrorProtocol'},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_download': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'protocol': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'})
        },
        'mirrors.mirrorrsync': {
            'Meta': {'object_name': 'MirrorRsync'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'mirror': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rsync_ips'", 'to': "orm['mirrors.Mirror']"})
        },
        'mirrors.mirrorurl': {
            'Meta': {'object_name': 'MirrorUrl'},
            'country': ('mirrors.models.NullCharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'has_ipv4': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_ipv6': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mirror': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'urls'", 'to': "orm['mirrors.Mirror']"}),
            'protocol': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'urls'", 'on_delete': 'models.PROTECT', 'to': "orm['mirrors.MirrorProtocol']"}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['mirrors']
