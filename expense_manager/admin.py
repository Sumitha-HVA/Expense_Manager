from django.contrib import admin
from .models import Employee, Vendor, Expenses
# Register your models here.

admin.site.register(Employee)
admin.site.register(Vendor)
admin.site.register(Expenses)