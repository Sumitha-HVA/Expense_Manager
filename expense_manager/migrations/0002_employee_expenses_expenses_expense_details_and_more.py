# Generated by Django 4.0.4 on 2022-05-20 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expense_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='expenses',
            field=models.CharField(default='Some string', max_length=60),
        ),
        migrations.AddField(
            model_name='expenses',
            name='expense_details',
            field=models.ManyToManyField(to='expense_manager.vendor'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='employee_expenses',
            field=models.ForeignKey(default='Some String', on_delete=django.db.models.deletion.CASCADE, to='expense_manager.employee'),
        ),
    ]
