# Generated by Django 4.0.4 on 2022-05-20 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_manager', '0004_remove_vendor_employee_expenses_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='expenses',
        ),
        migrations.RemoveField(
            model_name='expenses',
            name='expense_details',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='employee_expenses',
        ),
    ]
