# Generated by Django 3.1.6 on 2021-02-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_employee_afaps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='lucky_number',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
    ]
