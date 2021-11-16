# Generated by Django 3.2.7 on 2021-11-16 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_cabs_reg_driver_reg'),
        ('users', '0004_auto_20211115_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel_booking',
            name='amount',
            field=models.CharField(max_length=255, null=True, verbose_name='amount'),
        ),
        migrations.AddField(
            model_name='hotel_booking',
            name='booking_id',
            field=models.CharField(max_length=255, null=True, verbose_name='booking_id'),
        ),
        migrations.AddField(
            model_name='hotel_booking',
            name='check_in_date',
            field=models.DateField(default='0', max_length=255, null=True, verbose_name='check_in_date'),
        ),
        migrations.AddField(
            model_name='hotel_booking',
            name='check_in_time',
            field=models.TimeField(default='0', max_length=255, null=True, verbose_name='check_in_time'),
        ),
        migrations.AddField(
            model_name='hotel_booking',
            name='check_out_date',
            field=models.DateField(default='0', max_length=255, null=True, verbose_name='check_out_date'),
        ),
        migrations.AddField(
            model_name='hotel_booking',
            name='check_out_time',
            field=models.TimeField(default='0', max_length=255, null=True, verbose_name='check_out_time'),
        ),
        migrations.AddField(
            model_name='hotel_booking',
            name='guest_no',
            field=models.CharField(max_length=255, null=True, verbose_name='guests'),
        ),
        migrations.AddField(
            model_name='hotel_booking',
            name='rooms',
            field=models.CharField(max_length=255, null=True, verbose_name='rooms'),
        ),
        migrations.RemoveField(
            model_name='hotel_booking',
            name='room_id',
        ),
        migrations.AddField(
            model_name='hotel_booking',
            name='room_id',
            field=models.ManyToManyField(related_name='hotel_rooms', to='clients.Room_Register'),
        ),
    ]
