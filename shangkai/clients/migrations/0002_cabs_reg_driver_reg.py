# Generated by Django 3.2.7 on 2021-11-15 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Driver_Reg",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "datetime",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "driver_id",
                    models.CharField(
                        max_length=255, null=True, verbose_name="driver_id"
                    ),
                ),
                (
                    "driver_name",
                    models.CharField(
                        max_length=255, null=True, verbose_name="driver_name"
                    ),
                ),
                (
                    "driver_address",
                    models.CharField(
                        max_length=255, null=True, verbose_name="driver_address"
                    ),
                ),
                (
                    "driver_mobile",
                    models.CharField(
                        max_length=255, null=True, verbose_name="driver_mobile"
                    ),
                ),
                (
                    "driver_email",
                    models.CharField(
                        max_length=255, null=True, verbose_name="driver_email"
                    ),
                ),
                (
                    "languages",
                    models.CharField(
                        max_length=255, null=True, verbose_name="languages"
                    ),
                ),
                (
                    "working_hours",
                    models.CharField(
                        max_length=255, null=True, verbose_name="working_hours"
                    ),
                ),
                (
                    "licence_no",
                    models.CharField(
                        max_length=255, null=True, verbose_name="licence_no"
                    ),
                ),
                (
                    "driver_doc",
                    models.FileField(
                        default="driver_avatar.jpg",
                        max_length=255,
                        null=True,
                        upload_to="drivers/",
                        verbose_name="driver_doc",
                    ),
                ),
                (
                    "picture",
                    models.FileField(
                        default="driver_avatar.jpg",
                        max_length=255,
                        null=True,
                        upload_to="",
                        verbose_name="picture",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="status"
                    ),
                ),
            ],
            options={
                "verbose_name": "Car Driver Registration",
                "verbose_name_plural": "Car Driver Registration",
            },
        ),
        migrations.CreateModel(
            name="Cabs_Reg",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "datetime",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "car_code",
                    models.CharField(
                        max_length=255, null=True, verbose_name="car_code"
                    ),
                ),
                (
                    "car_name",
                    models.CharField(
                        max_length=255, null=True, verbose_name="car_name"
                    ),
                ),
                (
                    "car_type",
                    models.CharField(
                        max_length=255, null=True, verbose_name="car_type"
                    ),
                ),
                (
                    "capacity",
                    models.CharField(
                        max_length=255, null=True, verbose_name="capacity"
                    ),
                ),
                (
                    "vehicle_no",
                    models.CharField(
                        max_length=255, null=True, verbose_name="vehicle_no"
                    ),
                ),
                (
                    "car_mou",
                    models.CharField(max_length=255, null=True, verbose_name="car_mou"),
                ),
                (
                    "pickup_point",
                    models.CharField(
                        max_length=255, null=True, verbose_name="pickup_point"
                    ),
                ),
                (
                    "car_rating",
                    models.CharField(
                        max_length=255, null=True, verbose_name="car_rating"
                    ),
                ),
                (
                    "car_doc",
                    models.FileField(
                        default="car_doc.jpg",
                        max_length=255,
                        null=True,
                        upload_to="cab_doc/",
                        verbose_name="car_doc",
                    ),
                ),
                (
                    "car_images",
                    models.FileField(
                        default="car_image.jpg",
                        max_length=255,
                        null=True,
                        upload_to="cab_image/",
                        verbose_name="car_images",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="status"
                    ),
                ),
                (
                    "driver",
                    models.ForeignKey(
                        db_constraint=False,
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clients.driver_reg",
                    ),
                ),
            ],
            options={
                "verbose_name": "Car Registration",
                "verbose_name_plural": "Car Registration",
            },
        ),
    ]
