# Generated by Django 3.1.6 on 2021-03-09 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_auto_20210307_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='position_other',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]