# Generated by Django 3.0 on 2019-12-16 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='university',
        ),
    ]
