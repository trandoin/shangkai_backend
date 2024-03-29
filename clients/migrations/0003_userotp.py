# Generated by Django 4.1.1 on 2022-10-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserOTP",
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
                ("otp", models.CharField(max_length=6)),
                ("mobile", models.CharField(max_length=10)),
                (
                    "session_id",
                    models.CharField(max_length=255, verbose_name="session_id"),
                ),
                (
                    "used_for",
                    models.CharField(
                        choices=[("login", "login"), ("forgot", "forgot")],
                        max_length=255,
                        verbose_name="used_for",
                    ),
                ),
            ],
        ),
    ]
