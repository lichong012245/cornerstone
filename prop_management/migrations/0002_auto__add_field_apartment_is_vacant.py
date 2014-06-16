# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Apartment.is_vacant'
        db.add_column(u'prop_management_apartment', 'is_vacant',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Apartment.is_vacant'
        db.delete_column(u'prop_management_apartment', 'is_vacant')


    models = {
        u'prop_management.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_vacant': ('django.db.models.fields.BooleanField', [], {}),
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