# Generated by Django 3.1.6 on 2021-03-25 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_lessonlearn_airport'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonlearn',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=300),
        ),
    ]