# Generated by Django 2.1.2 on 2018-12-06 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songr', '0005_songupload_dejay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songupload',
            name='dejay',
        ),
    ]