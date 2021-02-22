# Generated by Django 3.1.6 on 2021-02-18 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=10)),
                ('job', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_division', to='myapp.division')),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_division', to='myapp.division')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_eng', models.CharField(blank=True, max_length=64, null=True)),
                ('first_name_thai', models.CharField(blank=True, max_length=64, null=True)),
                ('last_name_eng', models.CharField(blank=True, max_length=64, null=True)),
                ('last_name_thai', models.CharField(blank=True, max_length=64, null=True)),
                ('date_birth', models.DateField(default=None)),
                ('line_id', models.CharField(blank=True, max_length=20, null=True)),
                ('telephone', models.CharField(blank=True, help_text='your number 10 number', max_length=10, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('picture', models.ImageField(upload_to='')),
                ('division', models.ManyToManyField(blank=True, related_name='employee_division', to='myapp.Division')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]