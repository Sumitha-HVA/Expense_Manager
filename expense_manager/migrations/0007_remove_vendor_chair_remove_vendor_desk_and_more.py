# Generated by Django 4.0.4 on 2022-05-20 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_manager', '0006_expenses_emp_code_expenses_vend_code_vendor_chair_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='chair',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='desk',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='laptop',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='wifi',
        ),
    ]