# Generated by Django 3.2.8 on 2021-10-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211030_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
