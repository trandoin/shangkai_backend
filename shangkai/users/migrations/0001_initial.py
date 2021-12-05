# Generated by Django 3.2.7 on 2021-11-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Normal_UserReg",
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
                    "user_id",
                    models.CharField(max_length=255, null=True, verbose_name="user_id"),
                ),
                (
                    "user_ip",
                    models.CharField(max_length=255, null=True, verbose_name="user_ip"),
                ),
                (
                    "name",
                    models.CharField(max_length=255, null=True, verbose_name="name"),
                ),
                (
                    "email",
                    models.EmailField(max_length=255, null=True, verbose_name="email"),
                ),
                (
                    "mobile",
                    models.CharField(max_length=255, null=True, verbose_name="mobile"),
                ),
                (
                    "password",
                    models.CharField(
                        max_length=255, null=True, verbose_name="password"
                    ),
                ),
                (
                    "image",
                    models.FileField(
                        default="user_avatar.jpg",
                        max_length=255,
                        null=True,
                        upload_to="",
                        verbose_name="image",
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
                "verbose_name": "Normal User Registration",
                "verbose_name_plural": "Normal User Registration",
            },
        ),
    ]
