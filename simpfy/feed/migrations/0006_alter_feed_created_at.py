# Generated by Django 4.1 on 2022-11-04 07:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_alter_feed_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 15, 32, 52, 399490)),
        ),
    ]
