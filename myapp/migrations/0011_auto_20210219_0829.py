# Generated by Django 3.1.6 on 2021-02-19 01:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20210219_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='update',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
