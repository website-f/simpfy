# Generated by Django 4.1 on 2022-11-15 02:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0038_alter_feed_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 15, 10, 11, 8, 130371)),
        ),
    ]