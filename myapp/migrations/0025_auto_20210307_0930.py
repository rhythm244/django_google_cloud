# Generated by Django 3.1.6 on 2021-03-07 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_employee_is_pilot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_birth',
            field=models.DateField(default=None, null=True),
        ),
    ]
