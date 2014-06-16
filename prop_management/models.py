from django.db import models

class PropertyBundle(models.Model):
     name = models.CharField(max_length=225,blank=True,null=True)
     description=models.TextField(blank=True)

     def __unicode__(self):
        return self.name


class PropertyManager(models.Model):
    first_name=models.CharField(max_length=100,blank=True,null=True)
    last_name=models.CharField(max_length=100,blank=True,null=True)
    address=models.CharField(max_length=225,blank=True,null=True)
    firm_name=models.CharField(max_length=100,blank=True,null=True)

    def __unicode__(self):
        return "%s %s from %s" % (self.first_name,self.last_name,self.firm_name)


class Property(models.Model):
    address=models.CharField(max_length=225)
    block_lot=models.CharField(max_length=30,blank=True)
    sqrf=models.IntegerField(blank=True)
    year_built=models.IntegerField(blank=True)
    number_of_units=models.IntegerField()
    property_manager=models.ForeignKey(PropertyManager,blank=True,null=True)
    bundle=models.ForeignKey(PropertyBundle,blank=True,null=True)

    class Meta:
       db_table = 'Properties'

    def __unicode__(self):
        return self.address

class Apartment(models.Model):
    property = models.ForeignKey(Property)
    alias=models.CharField(max_length=225)
    num_of_bedroom=models.IntegerField()
    num_of_bathroom=models.IntegerField()
    rent=models.IntegerField()
    is_vacant=models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s on %s' % (self.alias, self.property.address)


class Tenant(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    apartment=models.ForeignKey(Apartment)
    phone=models.CharField(max_length=15,blank=True)
    security_deposit=models.IntegerField(blank=True,null=True)
    start=models.DateField(blank =True,null=True)
    end=models.DateField(blank=True,null=True)
    is_current=models.BooleanField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def property(self):
        return self.apartment.property

class RentIncome(models.Model):
    tenant=models.ForeignKey(Tenant)
    apartment=models.ForeignKey(Apartment)
    amount=models.IntegerField()
    date=models.DateField()
    is_full_for_current_month=models.BooleanField(blank=True)
    is_check=models.BooleanField(blank=True)
    check_number=models.CharField(max_length=30,blank=True)
    is_check_valid=models.BooleanField(blank=True)
    date_year_month=models.CharField(max_length=7,blank=True)

    def __unicode__(self):
        return str(self.amount)

    def save(self, *args, **kwargs):
        self.created_year=self.date.year
        self.created_month='%02d'%self.date.month
        self.date_year_month=str(self.created_year)+'-'+str(self.created_month)
        super(RentIncome, self).save()


class ExpenseType(models.Model):
    type=models.CharField(max_length=225)
    description=models.TextField(blank=True)

    def __unicode__(self):
        return self.type


class Vendor(models.Model):
    name=models.CharField(max_length=225)
    address=models.CharField(max_length=225,blank=True)

    def __unicode__(self):
        return self.name

class Account(models.Model):
    account=models.CharField(max_length=225)
    vendor=models.ForeignKey(Vendor)
    property=models.ForeignKey(Property,blank=True,null=True)
    description=models.TextField(blank=True)

    def __unicode__(self):
        return '%s:%s' % (self.account,self.property)

class Expense(models.Model):
    expense_type=models.ForeignKey(ExpenseType)
    property=models.ForeignKey(Property,blank=True,null=True)
    bundle=models.ForeignKey(PropertyBundle,blank=True,null=True)
    apartment=models.ForeignKey(Apartment,blank=True,null=True)
    vendor=models.ForeignKey(Vendor,blank=True,null=True)
    account=models.ForeignKey(Account,blank=True,null=True)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateField(blank=True,null=True)
    description=models.TextField(blank=True)






