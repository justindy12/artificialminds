# Generated by Django 4.0.1 on 2022-04-20 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0012_auto_20220413_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='meeting_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 20, 18, 59, 21, 741650)),
        ),
    ]
