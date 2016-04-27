from django.db import models

class Category(models.Model):
    name  =  models.CharField(max_length = 50)
    def __unicode__( self ):
        return self.name

class ExpensesRegistry(models.Model):
    expenses =  models.CharField(max_length = 50)
    income = models.CharField(max_length = 50)
    income_date = models.DateTimeField()
    expenses_date = models.DateTimeField()
    expenses_concept = models.TextField(max_length = 50)
    income_concept = models.TextField(max_length = 50)
    category = models.ForeignKey('Category')


class Husband(models.Model):
    age = models.IntegerField(max_length = 3)
    name = models.CharField(max_length = 50)

class Wife(models.Model):
    husband = models.OneToOneField(Husband)
    age = models.IntegerField(max_length = 3)
    name = models.CharField(max_length = 50)

class Children(models.Model):
    mother = models.ForeignKey(Wife, related_name = "children")
    name = models.CharField(max_length = 50)
    age = models.IntegerField(max_length = 3)

