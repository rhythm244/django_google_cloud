# Generated by Django 3.1.7 on 2021-04-18 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0041_auto_20210409_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonlearn',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
    ]