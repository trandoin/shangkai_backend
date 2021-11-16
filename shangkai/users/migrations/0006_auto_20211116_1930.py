# Generated by Django 3.2.7 on 2021-11-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211116_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_booking',
            name='check_in_date',
            field=models.DateField(max_length=255, null=True, verbose_name='check_in_date'),
        ),
        migrations.AlterField(
            model_name='hotel_booking',
            name='check_in_time',
            field=models.TimeField(max_length=255, null=True, verbose_name='check_in_time'),
        ),
        migrations.AlterField(
            model_name='hotel_booking',
            name='check_out_date',
            field=models.DateField(max_length=255, null=True, verbose_name='check_out_date'),
        ),
        migrations.AlterField(
            model_name='hotel_booking',
            name='check_out_time',
            field=models.TimeField(max_length=255, null=True, verbose_name='check_out_time'),
        ),
    ]
