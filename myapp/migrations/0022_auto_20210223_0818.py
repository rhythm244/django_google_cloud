# Generated by Django 3.1.6 on 2021-02-23 01:18

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20210222_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='employee_image',
            field=models.ImageField(upload_to='image/', validators=[myapp.models.validate_image], verbose_name='Image'),
        ),
    ]