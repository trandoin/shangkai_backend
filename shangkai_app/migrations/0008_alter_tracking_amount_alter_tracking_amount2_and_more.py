# Generated by Django 4.1.1 on 2022-10-15 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shangkai_app", "0007_remove_tracking_bookings_transaction_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tracking",
            name="amount",
            field=models.CharField(max_length=255, null=True, verbose_name="amount a"),
        ),
        migrations.AlterField(
            model_name="tracking",
            name="amount2",
            field=models.CharField(max_length=255, null=True, verbose_name="amount b"),
        ),
        migrations.CreateModel(
            name="Tracking_Order",
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
                ("seats", models.CharField(max_length=255, verbose_name="seats")),
                ("is_stay", models.BooleanField(default=False, verbose_name="is_stay")),
                ("currency", models.CharField(max_length=3, verbose_name="currency")),
                ("amount", models.CharField(max_length=255, verbose_name="amount")),
                (
                    "tracking",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shangkai_app.tracking",
                    ),
                ),
            ],
        ),
    ]
