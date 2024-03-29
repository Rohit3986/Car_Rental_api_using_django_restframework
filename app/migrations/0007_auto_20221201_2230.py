# Generated by Django 3.2.16 on 2022-12-01 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_images',
            field=models.FileField(upload_to='E:\\pythonproject\\django\\django rest framework\\VehicleRentalApi\\cars'),
        ),
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BookingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_status', models.CharField(choices=[('1', 'pending'), ('2', 'not approved'), ('3', 'approved')], max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True)),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='renter', to=settings.AUTH_USER_MODEL)),
                ('requested_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
