# Generated by Django 4.1 on 2022-11-08 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0008_alter_profile_image'),
        ('tools', '0003_rembg_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rembg',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prof.profile'),
        ),
    ]