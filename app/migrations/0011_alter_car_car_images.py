# Generated by Django 3.2.16 on 2022-12-02 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_bookingrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_images',
            field=models.FileField(blank=True, upload_to='E:\\pythonproject\\django\\django rest framework\\VehicleRentalApi\\cars'),
        ),
    ]