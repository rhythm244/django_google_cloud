# Generated by Django 3.1.6 on 2021-02-19 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20210219_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='afaps',
            field=models.IntegerField(default=None),
        ),
    ]
