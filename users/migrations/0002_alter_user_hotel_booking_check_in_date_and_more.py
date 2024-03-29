# Generated by Django 4.1.1 on 2022-10-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_hotel_booking",
            name="check_in_date",
            field=models.DateField(
                max_length=255, null=True, verbose_name="check_in_date"
            ),
        ),
        migrations.AlterField(
            model_name="user_hotel_booking",
            name="check_in_time",
            field=models.TimeField(
                max_length=255, null=True, verbose_name="check_in_time"
            ),
        ),
        migrations.AlterField(
            model_name="user_hotel_booking",
            name="check_out_date",
            field=models.DateField(
                max_length=255, null=True, verbose_name="check_out_date"
            ),
        ),
        migrations.AlterField(
            model_name="user_hotel_booking",
            name="check_out_time",
            field=models.TimeField(
                default="0", max_length=255, null=True, verbose_name="check_out_time"
            ),
        ),
        migrations.AlterField(
            model_name="user_hotel_booking",
            name="guest_no",
            field=models.IntegerField(default=1, null=True, verbose_name="guests"),
        ),
        migrations.AlterField(
            model_name="user_hotel_booking",
            name="rooms",
            field=models.IntegerField(default=1, null=True, verbose_name="rooms"),
        ),
    ]
