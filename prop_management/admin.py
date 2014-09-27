from django.contrib import admin
from prop_management.models import *
from django import forms
from actions import export_as_csv_action
from django.db.models import Sum
from django.contrib.admin.views.main import ChangeList

class PropertyManagerAdmin(admin.ModelAdmin):
   class meta:
    model = PropertyManager

class ExpenseTypeForm(forms.ModelForm):
    description =forms.CharField(widget=forms.Textarea)
    class meta:
        model = ExpenseType

class ExpenseTypeAdmin(admin.ModelAdmin):
    form = ExpenseTypeForm
    list_display=('type','description')


class ExpenseForm(forms.ModelForm):
    description =forms.CharField(widget=forms.Textarea)
    class meta:
        model = Expense

class ExpenseAdmin(admin.ModelAdmin):
    form = ExpenseForm
    list_per_page = 30
    list_display=('expense_type','property','apartment','account','vendor','amount','date','description','bundle')
    list_filter=('expense_type','vendor','property','bundle')
    list_editable=('amount','bundle','account','property')
    search_fields=('property__address','description',)
    actions=[export_as_csv_action("CSV Export", fields=list_display)]

    def get_changelist(self,request):
        return NewChangeList3


class NewChangeList(ChangeList): # for Apartment
        def get_results(self,*args,**kwargs):
            super(NewChangeList, self).get_results(*args, **kwargs)
            q = self.result_list.aggregate(total=Sum('rent'))
            self.total = q['total']

class NewChangeList2(ChangeList): # for Rent Income
        def get_results(self,*args,**kwargs):
            super(NewChangeList2, self).get_results(*args, **kwargs)
            q = self.result_list.aggregate(total=Sum('amount'))
            self.total = q['total']

class NewChangeList3(ChangeList): # for Expense
        def get_results(self,*args,**kwargs):
            super(NewChangeList3, self).get_results(*args, **kwargs)
            q = self.result_list.aggregate(total=Sum('amount'))
            self.total = q['total']

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('alias', 'property','num_of_bedroom','num_of_bathroom','rent','is_vacant')
    ordering=('property','id')
    list_filter=('is_vacant',)
    search_fields=('property__address',)
    actions=[export_as_csv_action("CSV Export", fields=list_display)]


    def get_changelist(self,request):
        return NewChangeList


class TenantAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','apartment','security_deposit','is_current')
    list_editable=('security_deposit',)
    actions=[export_as_csv_action("CSV Export", fields=list_display)]
    ordering=('id',)

class RentIncomeAdmin(admin.ModelAdmin):
    list_display=('tenant','apartment','amount','date_year_month','is_full_for_current_month')
    ordering=('id',)
    list_editable=('amount','is_full_for_current_month')
    list_filter=(('is_full_for_current_month',admin.BooleanFieldListFilter),'date_year_month','apartment__property','apartment__property__bundle')
    search_fields=('tenant__last_name','apartment__property__address',)
    actions=[export_as_csv_action("CSV Export", fields=list_display)]

    def get_changelist(self,request):
        return NewChangeList2

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account','vendor','property','description')

class PropertyBundleAdmin(admin.ModelAdmin):
    pass

class PropertyAdmin(admin.ModelAdmin):
    list_display=('address','bundle')
    list_filter=('bundle',)

# Register your models here.

admin.site.register(Property, PropertyAdmin)
admin.site.register(Apartment,ApartmentAdmin)
admin.site.register(Tenant,TenantAdmin)
admin.site.register(ExpenseType,ExpenseTypeAdmin)
admin.site.register(Vendor)
admin.site.register(Expense,ExpenseAdmin)
admin.site.register(RentIncome,RentIncomeAdmin)
admin.site.register(PropertyManager,PropertyManagerAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(PropertyBundle,PropertyBundleAdmin)
