# Generated by Django 3.1.6 on 2021-02-18 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='division',
            name='job',
        ),
        migrations.AlterField(
            model_name='position',
            name='job',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]