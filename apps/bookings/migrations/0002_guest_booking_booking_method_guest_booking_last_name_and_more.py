# Generated by Django 4.0.2 on 2022-02-15 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest_booking',
            name='booking_method',
            field=models.CharField(choices=[('PH', 'PHONE'), ('BK', 'BOOKING'), ('RE', 'LOBBY')], default='PH', max_length=15),
        ),
        migrations.AddField(
            model_name='guest_booking',
            name='last_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='guest_booking',
            name='name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='guest_booking',
            name='room',
            field=models.IntegerField(null=True),
        ),
    ]
