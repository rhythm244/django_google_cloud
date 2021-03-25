# Generated by Django 3.1.6 on 2021-03-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_auto_20210323_1402'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['first_name_thai']},
        ),
        migrations.AddField(
            model_name='lessonlearn',
            name='mission',
            field=models.CharField(choices=[('1', 'Domestic'), ('2', 'International')], default=None, max_length=20),
        ),
    ]
