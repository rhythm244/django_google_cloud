# Generated by Django 3.1.7 on 2021-04-09 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0037_auto_20210409_2008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['first_name_thai']},
        ),
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together=set(),
        ),
    ]