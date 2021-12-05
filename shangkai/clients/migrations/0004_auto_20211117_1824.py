# Generated by Django 3.2.7 on 2021-11-17 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0003_account_details"),
    ]

    operations = [
        migrations.AddField(
            model_name="cabs_reg",
            name="user",
            field=models.ForeignKey(
                db_constraint=False,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="clients.user_register",
            ),
        ),
        migrations.AddField(
            model_name="driver_reg",
            name="user",
            field=models.ForeignKey(
                db_constraint=False,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="clients.user_register",
            ),
        ),
    ]
