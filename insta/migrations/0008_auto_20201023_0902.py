# Generated by Django 3.1.2 on 2020-10-23 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0007_auto_20201023_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]