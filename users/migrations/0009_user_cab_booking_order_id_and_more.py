# Generated by Django 4.1.1 on 2022-11-15 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_user_guide_booking_order_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_cab_booking",
            name="order_id",
            field=models.CharField(max_length=255, null=True, verbose_name="order_id"),
        ),
        migrations.AddField(
            model_name="user_cab_booking",
            name="payment_id",
            field=models.CharField(
                max_length=255, null=True, verbose_name="payment_id"
            ),
        ),
        migrations.AddField(
            model_name="user_cab_booking",
            name="signature",
            field=models.CharField(max_length=255, null=True, verbose_name="signature"),
        ),
        migrations.AlterField(
            model_name="user_cab_booking",
            name="check_in_date",
            field=models.DateField(
                max_length=255, null=True, verbose_name="check_in_date"
            ),
        ),
        migrations.AlterField(
            model_name="user_cab_booking",
            name="check_in_time",
            field=models.TimeField(
                max_length=255, null=True, verbose_name="check_in_time"
            ),
        ),
        migrations.AlterField(
            model_name="user_cab_booking",
            name="check_out_date",
            field=models.DateField(
                max_length=255, null=True, verbose_name="check_out_date"
            ),
        ),
        migrations.AlterField(
            model_name="user_cab_booking",
            name="check_out_time",
            field=models.TimeField(
                max_length=255, null=True, verbose_name="check_out_time"
            ),
        ),
        migrations.AlterField(
            model_name="user_cab_cart",
            name="check_in_date",
            field=models.DateField(
                max_length=255, null=True, verbose_name="check_in_date"
            ),
        ),
        migrations.AlterField(
            model_name="user_cab_cart",
            name="check_in_time",
            field=models.TimeField(
                max_length=255, null=True, verbose_name="check_in_time"
            ),
        ),
        migrations.AlterField(
            model_name="user_cab_cart",
            name="check_out_date",
            field=models.DateField(
                max_length=255, null=True, verbose_name="check_out_date"
            ),
        ),
        migrations.AlterField(
            model_name="user_cab_cart",
            name="check_out_time",
            field=models.TimeField(
                max_length=255, null=True, verbose_name="check_out_time"
            ),
        ),
        migrations.CreateModel(
            name="User_Cab_Order",
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
                ("currency", models.CharField(max_length=255, verbose_name="currency")),
                ("amount", models.CharField(max_length=255, verbose_name="amount")),
                (
                    "cart_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.user_cab_cart",
                    ),
                ),
            ],
        ),
    ]
