# Generated by Django 2.2.1 on 2019-05-29 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190529_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='data_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
