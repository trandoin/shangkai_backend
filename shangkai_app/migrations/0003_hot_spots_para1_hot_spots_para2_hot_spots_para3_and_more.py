# Generated by Django 4.1.1 on 2022-09-29 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shangkai_app", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="hot_spots",
            name="para1",
            field=models.TextField(
                blank=True, max_length=2000, null=True, verbose_name="para1"
            ),
        ),
        migrations.AddField(
            model_name="hot_spots",
            name="para2",
            field=models.TextField(
                blank=True, max_length=2000, null=True, verbose_name="para2"
            ),
        ),
        migrations.AddField(
            model_name="hot_spots",
            name="para3",
            field=models.TextField(
                blank=True, max_length=2000, null=True, verbose_name="para3"
            ),
        ),
        migrations.AddField(
            model_name="hot_spots",
            name="title_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="hotspot_images",
                verbose_name="title_image",
            ),
        ),
        migrations.AddField(
            model_name="hot_spots",
            name="transport",
            field=models.CharField(max_length=255, null=True, verbose_name="transport"),
        ),
        migrations.CreateModel(
            name="HotSpot_Images",
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
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="hotspot_images",
                        verbose_name="image",
                    ),
                ),
                (
                    "hotspot",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shangkai_app.hot_spots",
                    ),
                ),
            ],
            options={
                "verbose_name": "Hotspot Images",
                "verbose_name_plural": "Hotspot Images",
            },
        ),
    ]
