# Generated by Django 3.0.8 on 2020-11-11 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200710_0118'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
