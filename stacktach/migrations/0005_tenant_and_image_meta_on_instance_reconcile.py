# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'InstanceReconcile.tenant'
        db.add_column(u'stacktach_instancereconcile', 'tenant',
                      self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InstanceReconcile.os_architecture'
        db.add_column(u'stacktach_instancereconcile', 'os_architecture',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'InstanceReconcile.os_distro'
        db.add_column(u'stacktach_instancereconcile', 'os_distro',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'InstanceReconcile.os_version'
        db.add_column(u'stacktach_instancereconcile', 'os_version',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'InstanceReconcile.rax_options'
        db.add_column(u'stacktach_instancereconcile', 'rax_options',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'InstanceReconcile.tenant'
        db.delete_column(u'stacktach_instancereconcile', 'tenant')

        # Deleting field 'InstanceReconcile.os_architecture'
        db.delete_column(u'stacktach_instancereconcile', 'os_architecture')

        # Deleting field 'InstanceReconcile.os_distro'
        db.delete_column(u'stacktach_instancereconcile', 'os_distro')

        # Deleting field 'InstanceReconcile.os_version'
        db.delete_column(u'stacktach_instancereconcile', 'os_version')

        # Deleting field 'InstanceReconcile.rax_options'
        db.delete_column(u'stacktach_instancereconcile', 'rax_options')


    models = {
        u'stacktach.deployment': {
            'Meta': {'object_name': 'Deployment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'stacktach.instancedeletes': {
            'Meta': {'object_name': 'InstanceDeletes'},
            'deleted_at': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '6', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'launched_at': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '6', 'db_index': 'True'}),
            'raw': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stacktach.RawData']", 'null': 'True'})
        },
        u'stacktach.instanceexists': {
            'Meta': {'object_name': 'InstanceExists'},
            'audit_period_beginning': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '6', 'db_index': 'True'}),
            'audit_period_ending': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '6', 'db_index': 'True'}),
            'delete': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['stacktach.InstanceDeletes']"}),
            'deleted_at': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '6', 'db_index': 'True'}),
            'fail_reason': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'instance_type_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'launched_at': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '6', 'db_index': 'True'}),
            'message_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'os_architecture': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'os_distro': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'os_version': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'raw': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['stacktach.RawData']"}),
            'rax_options': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'send_status': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '50', 'db_index': 'True'}),
            'tenant': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'usage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['stacktach.InstanceUsage']"})
        },
        u'stacktach.instancereconcile': {
            'Meta': {'object_name': 'InstanceReconcile'},
            'deleted_at': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '6', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'instance_type_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'launched_at': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '6', 'db_index': 'True'}),
            'os_architecture': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'os_distro': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'os_version': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rax_options': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'row_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'row_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'tenant': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'stacktach.instanceusage': {
            'Meta': {'object_name': 'InstanceUsage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'instance_type_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'launched_at': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '6', 'db_index': 'True'}),
            'os_architecture': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'os_distro': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'os_version': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rax_options': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'request_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tenant': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'stacktach.jsonreport': {
            'Meta': {'object_name': 'JsonReport'},
            'created': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '6', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'period_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'period_start': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'stacktach.lifecycle': {
            'Meta': {'object_name': 'Lifecycle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'last_raw': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stacktach.RawData']", 'null': 'True'}),
            'last_state': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'last_task_state': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'stacktach.rawdata': {
            'Meta': {'object_name': 'RawData'},
            'deployment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stacktach.Deployment']"}),
            'event': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_type': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True'}),
            'instance': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {}),
            'old_state': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'old_task': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'request_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'routing_key': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'service': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'tenant': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'when': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '6', 'db_index': 'True'})
        },
        u'stacktach.rawdataimagemeta': {
            'Meta': {'object_name': 'RawDataImageMeta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'os_architecture': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'os_distro': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'os_version': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'raw': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stacktach.RawData']"}),
            'rax_options': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'stacktach.requesttracker': {
            'Meta': {'object_name': 'RequestTracker'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'duration': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '6', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_timing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stacktach.Timing']", 'null': 'True'}),
            'lifecycle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stacktach.Lifecycle']"}),
            'request_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'start': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '6', 'db_index': 'True'})
        },
        u'stacktach.timing': {
            'Meta': {'object_name': 'Timing'},
            'diff': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '6', 'db_index': 'True'}),
            'end_raw': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['stacktach.RawData']"}),
            'end_when': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lifecycle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stacktach.Lifecycle']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'start_raw': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['stacktach.RawData']"}),
            'start_when': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '6'})
        }
    }

    complete_apps = ['stacktach']
