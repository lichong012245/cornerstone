from django.db import models


class Properties(models.Model):
    address=models.CharField(max_length=100)
    block_lot=models.CharField(max_length=30,blank=True)
    sqrf=models.IntegerField(blank=True)
    year_built=models.IntegerField(blank=True)
    number_of_units=models.IntegerField()

    def __unicode__(self):
        return self.address


class Apartments(models.Model):
    property = models.ForeignKey(Properties)
    alias=models.CharField(max_length=10)
    num_of_bedroom=models.IntegerField()
    num_of_bathroom=models.IntegerField()
    rent=models.IntegerField()

    def __unicode__(self):
        return self.alias


class Tenants(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    apartment=models.ForeignKey(Apartments)
    phone=models.CharField(blank=True)
    start=models.DateField(blank =True,null=True)
    end=models.DateField(blank=True,null=True)

    def __unicode__(self):
        return self.last_name

class RentIncome(models.Model):
    tenant=models.ForeignKey(Tenants)
    apartment=models.ForeignKey(Apartments)
    amount=models.IntegerField()
    date=models.DateField()
    is_full_for_current_month=models.BooleanField(blank=True)
    is_check=models.BooleanField(blank=True)
    check_number=models.CharField(blank=True)
    is_check_valid=models.BooleanField(blank=True)
    date_year_month=models.CharField(max_length=7)

    def __unicode__(self):
        return self.amount

    def save(self, *args, **kwargs):
        self.created_year=self.date.year
        self.created_month='%02d'%self.date.month
        self.date_year_month=str(self.created_year)+'-'+str(self.created_month)
        super(post, self).save()


class Expense_type(models.Model):
    type=models.CharField()

    def __unicode__(self):
        return self.type


class Vendor(models.Model):
    name=models.CharField()
    address=models.CharField(blank=True)

    def __unicode__(self):
        return self.name

class Expenses(models.Model):
    expense_type=models.ForeignKey(expense_type)
    property=models.ForeignKey(Properties,blank=True,null=True)
    apartment=models.ForeignKey(Apartments,blank=True,null=True)
    vendor=models.ForeignKey(Vendor,blank=True,null=True)
    description=models.TextField()
    amount=models.DecimalField(decimal_places=2)





