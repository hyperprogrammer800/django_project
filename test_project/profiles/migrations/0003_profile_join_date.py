# Generated by Django 4.1.4 on 2022-12-11 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_contact_profile_contact_ext_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='join_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]