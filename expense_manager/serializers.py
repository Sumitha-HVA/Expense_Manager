from rest_framework import serializers
from .models import Employee, Vendor, Expenses

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('name', 'emp_code')


class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = ('name', 'vend_code','emp_code')


class ExpensesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expenses
        fields = ('expense_comment', 'expense_done_on', 'expense_amount', 'emp_code', 'vend_code')