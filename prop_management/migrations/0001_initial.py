# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Property'
        db.create_table('prop_management_properties', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('block_lot', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('sqrf', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('year_built', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('number_of_units', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'prop_management', ['Property'])

        # Adding model 'Apartment'
        db.create_table(u'prop_management_apartment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prop_management.Property'])),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('num_of_bedroom', self.gf('django.db.models.fields.IntegerField')()),
            ('num_of_bathroom', self.gf('django.db.models.fields.IntegerField')()),
            ('rent', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'prop_management', ['Apartment'])

        # Adding model 'Tenant'
        db.create_table(u'prop_management_tenant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prop_management.Apartment'])),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('is_current', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'prop_management', ['Tenant'])

        # Adding model 'RentIncome'
        db.create_table(u'prop_management_rentincome', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tenant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prop_management.Tenant'])),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prop_management.Apartment'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('is_full_for_current_month', self.gf('django.db.models.fields.BooleanField')()),
            ('is_check', self.gf('django.db.models.fields.BooleanField')()),
            ('check_number', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('is_check_valid', self.gf('django.db.models.fields.BooleanField')()),
            ('date_year_month', self.gf('django.db.models.fields.CharField')(max_length=7)),
        ))
        db.send_create_signal(u'prop_management', ['RentIncome'])

        # Adding model 'ExpenseType'
        db.create_table(u'prop_management_expensetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'prop_management', ['ExpenseType'])

        # Adding model 'Vendor'
        db.create_table(u'prop_management_vendor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'prop_management', ['Vendor'])

        # Adding model 'Expense'
        db.create_table(u'prop_management_expense', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('expense_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prop_management.ExpenseType'])),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prop_management.Property'], null=True, blank=True)),
            ('apartment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prop_management.Apartment'], null=True, blank=True)),
            ('vendor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prop_management.Vendor'], null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'prop_management', ['Expense'])


    def backwards(self, orm):
        # Deleting model 'Property'
        db.delete_table('Properties')

        # Deleting model 'Apartment'
        db.delete_table(u'prop_management_apartment')

        # Deleting model 'Tenant'
        db.delete_table(u'prop_management_tenant')

        # Deleting model 'RentIncome'
        db.delete_table(u'prop_management_rentincome')

        # Deleting model 'ExpenseType'
        db.delete_table(u'prop_management_expensetype')

        # Deleting model 'Vendor'
        db.delete_table(u'prop_management_vendor')

        # Deleting model 'Expense'
        db.delete_table(u'prop_management_expense')


    models = {
        u'prop_management.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_of_bathroom': ('django.db.models.fields.IntegerField', [], {}),
            'num_of_bedroom': ('django.db.models.fields.IntegerField', [], {}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.Property']"}),
            'rent': ('django.db.models.fields.IntegerField', [], {})
        },
        u'prop_management.expense': {
            'Meta': {'object_name': 'Expense'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.Apartment']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'expense_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.ExpenseType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.Property']", 'null': 'True', 'blank': 'True'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.Vendor']", 'null': 'True', 'blank': 'True'})
        },
        u'prop_management.expensetype': {
            'Meta': {'object_name': 'ExpenseType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'prop_management.property': {
            'Meta': {'object_name': 'Property', 'db_table': "'Properties'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'block_lot': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_units': ('django.db.models.fields.IntegerField', [], {}),
            'sqrf': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'year_built': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        u'prop_management.rentincome': {
            'Meta': {'object_name': 'RentIncome'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.Apartment']"}),
            'check_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_year_month': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_check': ('django.db.models.fields.BooleanField', [], {}),
            'is_check_valid': ('django.db.models.fields.BooleanField', [], {}),
            'is_full_for_current_month': ('django.db.models.fields.BooleanField', [], {}),
            'tenant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.Tenant']"})
        },
        u'prop_management.tenant': {
            'Meta': {'object_name': 'Tenant'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.Apartment']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_current': ('django.db.models.fields.BooleanField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        u'prop_management.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['prop_management']