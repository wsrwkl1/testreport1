# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BL_mi2s'
        db.create_table('BL_mi2s', (
            ('Game', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Music', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('PlayVideo', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('ReadBook', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('WeiBO', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('CallMO', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Brower', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Camera', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Remain', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('Version', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
        ))
        db.send_create_signal(u'TRR', ['BL_mi2s'])

        # Adding model 'BL_mi2a'
        db.create_table('BL_mi2a', (
            ('Game', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Music', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('PlayVideo', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('ReadBook', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('WeiBO', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('CallMO', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Brower', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Camera', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Remain', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('Version', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
        ))
        db.send_create_signal(u'TRR', ['BL_mi2a'])

        # Adding model 'BL_mi3w'
        db.create_table('BL_mi3w', (
            ('Game', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Music', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('PlayVideo', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('ReadBook', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('WeiBO', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('CallMO', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Brower', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Camera', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Remain', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('Version', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
        ))
        db.send_create_signal(u'TRR', ['BL_mi3w'])

        # Adding model 'BL_mi3td'
        db.create_table('BL_mi3td', (
            ('Game', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Music', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('PlayVideo', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('ReadBook', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('WeiBO', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('CallMO', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Brower', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Camera', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Remain', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('Version', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
        ))
        db.send_create_signal(u'TRR', ['BL_mi3td'])

        # Adding model 'Current_mi2s'
        db.create_table('Current_mi2s', (
            ('Item1', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item2', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item3', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item4', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item5', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item6', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item7', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item8', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item9', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item10', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item11', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item12', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item13', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item14', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item15', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item16', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item17', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item18', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item19', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item20', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item21', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('Version', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
        ))
        db.send_create_signal(u'TRR', ['Current_mi2s'])

        # Adding model 'Current_mi2a'
        db.create_table('Current_mi2a', (
            ('Item1', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item2', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item3', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item4', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item5', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item6', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item7', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item8', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item9', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item10', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item11', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item12', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item13', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item14', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item15', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item16', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item17', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item18', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item19', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item20', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item21', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('Version', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
        ))
        db.send_create_signal(u'TRR', ['Current_mi2a'])

        # Adding model 'Current_mi3w'
        db.create_table('Current_mi3w', (
            ('Item1', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item2', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item3', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item4', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item5', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item6', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item7', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item8', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item9', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item10', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item11', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item12', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item13', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item14', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item15', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item16', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item17', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item18', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item19', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item20', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item21', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('Version', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
        ))
        db.send_create_signal(u'TRR', ['Current_mi3w'])

        # Adding model 'Current_mi3td'
        db.create_table('Current_mi3td', (
            ('Item1', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item2', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item3', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item4', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item5', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item6', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item7', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item8', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item9', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item10', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item11', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item12', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item13', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item14', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item15', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item16', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item17', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item18', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item19', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item20', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Item21', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('Version', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
        ))
        db.send_create_signal(u'TRR', ['Current_mi3td'])

        # Adding model 'CI_mi2s'
        db.create_table('CI_mi2s', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('BugID', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('priority', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('openversion', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('fixversion', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'TRR', ['CI_mi2s'])

        # Adding model 'CI_mi2a'
        db.create_table('CI_mi2a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('BugID', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('priority', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('openversion', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('fixversion', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'TRR', ['CI_mi2a'])

        # Adding model 'CI_mi3w'
        db.create_table('CI_mi3w', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('BugID', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('priority', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('openversion', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('fixversion', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'TRR', ['CI_mi3w'])

        # Adding model 'CI_mi3td'
        db.create_table('CI_mi3td', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('BugID', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('priority', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('openversion', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('fixversion', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'TRR', ['CI_mi3td'])

        # Adding model 'CC_mi2s'
        db.create_table('CC_mi2s', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('CaseName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Result', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Reason', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('Capacity', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('Trace', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Bugreport', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ScreenShot', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'TRR', ['CC_mi2s'])

        # Adding model 'CC_mi2a'
        db.create_table('CC_mi2a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('CaseName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Result', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Reason', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('Capacity', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('Trace', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Bugreport', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ScreenShot', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'TRR', ['CC_mi2a'])

        # Adding model 'CC_mi3w'
        db.create_table('CC_mi3w', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('CaseName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Result', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Reason', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('Capacity', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('Trace', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Bugreport', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ScreenShot', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'TRR', ['CC_mi3w'])

        # Adding model 'CC_mi3td'
        db.create_table('CC_mi3td', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('CaseName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Result', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Reason', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('Capacity', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('Trace', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Bugreport', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ScreenShot', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'TRR', ['CC_mi3td'])


    def backwards(self, orm):
        # Deleting model 'BL_mi2s'
        db.delete_table('BL_mi2s')

        # Deleting model 'BL_mi2a'
        db.delete_table('BL_mi2a')

        # Deleting model 'BL_mi3w'
        db.delete_table('BL_mi3w')

        # Deleting model 'BL_mi3td'
        db.delete_table('BL_mi3td')

        # Deleting model 'Current_mi2s'
        db.delete_table('Current_mi2s')

        # Deleting model 'Current_mi2a'
        db.delete_table('Current_mi2a')

        # Deleting model 'Current_mi3w'
        db.delete_table('Current_mi3w')

        # Deleting model 'Current_mi3td'
        db.delete_table('Current_mi3td')

        # Deleting model 'CI_mi2s'
        db.delete_table('CI_mi2s')

        # Deleting model 'CI_mi2a'
        db.delete_table('CI_mi2a')

        # Deleting model 'CI_mi3w'
        db.delete_table('CI_mi3w')

        # Deleting model 'CI_mi3td'
        db.delete_table('CI_mi3td')

        # Deleting model 'CC_mi2s'
        db.delete_table('CC_mi2s')

        # Deleting model 'CC_mi2a'
        db.delete_table('CC_mi2a')

        # Deleting model 'CC_mi3w'
        db.delete_table('CC_mi3w')

        # Deleting model 'CC_mi3td'
        db.delete_table('CC_mi3td')


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
            'Trace': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
            'Trace': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
            'Trace': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
            'Trace': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
        }
    }

    complete_apps = ['TRR']