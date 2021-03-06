# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PropertyBundle'
        db.create_table(u'prop_management_propertybundle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=225, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'prop_management', ['PropertyBundle'])

        # Adding model 'Account'
        db.create_table(u'prop_management_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.CharField')(max_length=225)),
            ('vendor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prop_management.Vendor'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'prop_management', ['Account'])

        # Adding field 'Expense.account'
        db.add_column(u'prop_management_expense', 'account',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prop_management.Account'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Property.bundle'
        db.add_column('Properties', 'bundle',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prop_management.PropertyBundle'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'PropertyBundle'
        db.delete_table(u'prop_management_propertybundle')

        # Deleting model 'Account'
        db.delete_table(u'prop_management_account')

        # Deleting field 'Expense.account'
        db.delete_column(u'prop_management_expense', 'account_id')

        # Deleting field 'Property.bundle'
        db.delete_column('Properties', 'bundle_id')


    models = {
        u'prop_management.account': {
            'Meta': {'object_name': 'Account'},
            'account': ('django.db.models.fields.CharField', [], {'max_length': '225'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.Vendor']"})
        },
        u'prop_management.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '225'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_vacant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'num_of_bathroom': ('django.db.models.fields.IntegerField', [], {}),
            'num_of_bedroom': ('django.db.models.fields.IntegerField', [], {}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.Property']"}),
            'rent': ('django.db.models.fields.IntegerField', [], {})
        },
        u'prop_management.expense': {
            'Meta': {'object_name': 'Expense'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.Account']", 'null': 'True', 'blank': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.Apartment']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expense_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.ExpenseType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.Property']", 'null': 'True', 'blank': 'True'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.Vendor']", 'null': 'True', 'blank': 'True'})
        },
        u'prop_management.expensetype': {
            'Meta': {'object_name': 'ExpenseType'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '225'})
        },
        u'prop_management.property': {
            'Meta': {'object_name': 'Property', 'db_table': "'Properties'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '225'}),
            'block_lot': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'bundle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.PropertyBundle']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_units': ('django.db.models.fields.IntegerField', [], {}),
            'property_manager': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.PropertyManager']", 'null': 'True', 'blank': 'True'}),
            'sqrf': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'year_built': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        u'prop_management.propertybundle': {
            'Meta': {'object_name': 'PropertyBundle'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '225', 'null': 'True', 'blank': 'True'})
        },
        u'prop_management.propertymanager': {
            'Meta': {'object_name': 'PropertyManager'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '225', 'null': 'True', 'blank': 'True'}),
            'firm_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'prop_management.rentincome': {
            'Meta': {'object_name': 'RentIncome'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prop_management.Apartment']"}),
            'check_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_year_month': ('django.db.models.fields.CharField', [], {'max_length': '7', 'blank': 'True'}),
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
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'security_deposit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'prop_management.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '225', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '225'})
        }
    }

    complete_apps = ['prop_management']