from tkinter import CASCADE
from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    emp_code = models.CharField(primary_key='True', max_length=100)
    
    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=30)
    vend_code = models.CharField(primary_key='True', max_length=100)
    emp_code = models.ForeignKey(Employee, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name


class Expenses(models.Model):
    expense_comment = models.CharField(max_length= 500)
    expense_done_on =models.DateField('Date of Expenses :')
    expense_amount = models.IntegerField()
    emp_code = models.ForeignKey(Employee, on_delete= models.CASCADE)
    vend_code = models.ForeignKey(Vendor, on_delete= models.CASCADE)

    def __str__(self):
        return self.expense_comment

