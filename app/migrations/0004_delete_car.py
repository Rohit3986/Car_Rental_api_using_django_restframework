# Generated by Django 3.2.16 on 2022-12-01 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_car'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Car',
        ),
    ]