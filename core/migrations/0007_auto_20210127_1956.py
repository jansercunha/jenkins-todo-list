# Generated by Django 2.1.7 on 2021-01-27 22:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210127_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 1, 27, 19, 56, 38, 576326)),
        ),
    ]
