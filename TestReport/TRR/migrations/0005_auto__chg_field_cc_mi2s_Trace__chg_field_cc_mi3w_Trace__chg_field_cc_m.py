# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CC_mi2s.Trace'
        db.alter_column('CC_mi2s', 'Trace', self.gf('django.db.models.fields.CharField')(max_length=1000))

        # Changing field 'CC_mi3w.Trace'
        db.alter_column('CC_mi3w', 'Trace', self.gf('django.db.models.fields.CharField')(max_length=1000))

        # Changing field 'CC_mi3td.Trace'
        db.alter_column('CC_mi3td', 'Trace', self.gf('django.db.models.fields.CharField')(max_length=1000))

        # Changing field 'CC_mi2a.Trace'
        db.alter_column('CC_mi2a', 'Trace', self.gf('django.db.models.fields.CharField')(max_length=1000))

    def backwards(self, orm):

        # Changing field 'CC_mi2s.Trace'
        db.alter_column('CC_mi2s', 'Trace', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'CC_mi3w.Trace'
        db.alter_column('CC_mi3w', 'Trace', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'CC_mi3td.Trace'
        db.alter_column('CC_mi3td', 'Trace', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'CC_mi2a.Trace'
        db.alter_column('CC_mi2a', 'Trace', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'TRR.bl_mi2a': {
            'Brower': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'CallMO': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Camera': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Game': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'BL_mi2a', 'db_table': "'BL_mi2a'"},
            'Music': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'PlayVideo': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'ReadBook': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Remain': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Version': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'WeiBO': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'TRR.bl_mi2s': {
            'Brower': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'CallMO': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Camera': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Game': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'BL_mi2s', 'db_table': "'BL_mi2s'"},
            'Music': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'PlayVideo': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'ReadBook': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Remain': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Version': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'WeiBO': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'TRR.bl_mi3td': {
            'Brower': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'CallMO': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Camera': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Game': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'BL_mi3td', 'db_table': "'BL_mi3td'"},
            'Music': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'PlayVideo': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'ReadBook': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Remain': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Version': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'WeiBO': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'TRR.bl_mi3w': {
            'Brower': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'CallMO': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Camera': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Game': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'BL_mi3w', 'db_table': "'BL_mi3w'"},
            'Music': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'PlayVideo': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'ReadBook': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Remain': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Version': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'WeiBO': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'TRR.cc_mi2a': {
            'Bugreport': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Capacity': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'CaseName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'CC_mi2a', 'db_table': "'CC_mi2a'"},
            'Reason': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Result': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ScreenShot': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Trace': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Version': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'TRR.cc_mi2s': {
            'Bugreport': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Capacity': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'CaseName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'CC_mi2s', 'db_table': "'CC_mi2s'"},
            'Reason': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Result': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ScreenShot': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Trace': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Version': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'TRR.cc_mi3td': {
            'Bugreport': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Capacity': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'CaseName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'CC_mi3td', 'db_table': "'CC_mi3td'"},
            'Reason': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Result': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ScreenShot': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Trace': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Version': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'TRR.cc_mi3w': {
            'Bugreport': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Capacity': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'CaseName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'CC_mi3w', 'db_table': "'CC_mi3w'"},
            'Reason': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Result': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ScreenShot': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Trace': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Version': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'TRR.ci_mi2a': {
            'BugID': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'CI_mi2a', 'db_table': "'CI_mi2a'"},
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fixversion': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'openversion': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'TRR.ci_mi2s': {
            'BugID': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'CI_mi2s', 'db_table': "'CI_mi2s'"},
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fixversion': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'openversion': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'TRR.ci_mi3td': {
            'BugID': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'CI_mi3td', 'db_table': "'CI_mi3td'"},
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fixversion': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'openversion': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'TRR.ci_mi3w': {
            'BugID': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'CI_mi3w', 'db_table': "'CI_mi3w'"},
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fixversion': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'openversion': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'TRR.current_mi2a': {
            'Item1': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item10': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item11': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item12': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item13': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item14': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item15': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item16': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item17': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item18': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item19': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item2': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item20': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item21': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item3': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item4': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item5': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item6': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item7': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item8': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item9': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'Current_mi2a', 'db_table': "'Current_mi2a'"},
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Version': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'})
        },
        u'TRR.current_mi2s': {
            'Item1': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item10': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item11': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item12': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item13': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item14': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item15': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item16': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item17': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item18': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item19': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item2': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item20': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item21': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item3': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item4': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item5': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item6': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item7': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item8': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item9': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'Current_mi2s', 'db_table': "'Current_mi2s'"},
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Version': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'})
        },
        u'TRR.current_mi3td': {
            'Item1': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item10': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item11': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item12': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item13': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item14': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item15': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item16': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item17': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item18': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item19': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item2': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item20': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item21': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item3': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item4': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item5': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item6': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item7': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item8': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item9': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'Current_mi3td', 'db_table': "'Current_mi3td'"},
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Version': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'})
        },
        u'TRR.current_mi3w': {
            'Item1': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item10': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item11': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item12': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item13': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item14': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item15': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item16': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item17': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item18': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item19': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item2': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item20': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item21': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item3': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item4': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item5': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item6': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item7': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item8': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Item9': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'Current_mi3w', 'db_table': "'Current_mi3w'"},
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Version': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'})
        },
        u'TRR.test_tb1': {
            'Meta': {'ordering': "('-Timestamp',)", 'object_name': 'test_tb1', 'db_table': "'test_tb1'"},
            'Timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'Version': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['TRR']