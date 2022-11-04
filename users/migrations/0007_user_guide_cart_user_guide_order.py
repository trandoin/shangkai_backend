# Generated by Django 4.1.1 on 2022-11-03 16:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0004_room_register_about"),
        ("users", "0006_user_hotel_booking_order_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="User_Guide_Cart",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "no_guests",
                    models.CharField(max_length=255, verbose_name="no_guests"),
                ),
                (
                    "booking_date",
                    models.DateField(max_length=255, verbose_name="booking_date"),
                ),
                (
                    "guide",
                    models.ForeignKey(
                        db_constraint=False,
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clients.tourguide_reg",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        db_constraint=False,
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.normal_userreg",
                    ),
                ),
            ],
            options={
                "verbose_name": "Guide Carts",
                "verbose_name_plural": "Guide Carts",
            },
        ),
        migrations.CreateModel(
            name="User_Guide_Order",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                        verbose_name="id",
                    ),
                ),
                ("currency", models.CharField(max_length=3, verbose_name="currency")),
                ("amount", models.CharField(max_length=255, verbose_name="amount")),
                (
                    "cart_item",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.user_guide_cart",
                    ),
                ),
            ],
        ),
    ]
