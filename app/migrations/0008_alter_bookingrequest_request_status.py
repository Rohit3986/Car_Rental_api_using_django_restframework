# Generated by Django 3.2.16 on 2022-12-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20221201_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrequest',
            name='request_status',
            field=models.CharField(choices=[('1', 'pending'), ('2', 'not approved'), ('3', 'approved')], default='1', max_length=10),
        ),
    ]
