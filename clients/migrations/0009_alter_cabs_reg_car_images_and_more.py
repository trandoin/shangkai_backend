# Generated by Django 4.1.1 on 2023-01-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0008_alter_tour_packages_location_ids_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cabs_reg",
            name="car_images",
            field=models.CharField(
                max_length=255, null=True, verbose_name="car_images"
            ),
        ),
        migrations.AlterField(
            model_name="cabs_reg",
            name="car_insurance",
            field=models.CharField(
                default="0", max_length=255, null=True, verbose_name="car_insurance"
            ),
        ),
        migrations.AlterField(
            model_name="cabs_reg",
            name="car_rc",
            field=models.CharField(
                default="0", max_length=255, null=True, verbose_name="car_rc"
            ),
        ),
        migrations.AlterField(
            model_name="driver_reg",
            name="adhar_card",
            field=models.CharField(
                default="0", max_length=255, null=True, verbose_name="addhar_card"
            ),
        ),
        migrations.AlterField(
            model_name="driver_reg",
            name="licence_doc",
            field=models.CharField(
                default="0", max_length=255, null=True, verbose_name="licence_doc"
            ),
        ),
        migrations.AlterField(
            model_name="driver_reg",
            name="picture",
            field=models.CharField(
                default="0", max_length=255, null=True, verbose_name="picture"
            ),
        ),
        migrations.AlterField(
            model_name="hotelimages",
            name="image",
            field=models.CharField(max_length=255, verbose_name="image"),
        ),
        migrations.AlterField(
            model_name="reg_hotel",
            name="title_image",
            field=models.CharField(
                max_length=255, null=True, verbose_name="title_image"
            ),
        ),
        migrations.AlterField(
            model_name="room_register",
            name="title_image",
            field=models.CharField(
                max_length=255, null=True, verbose_name="title_image"
            ),
        ),
        migrations.AlterField(
            model_name="roomimages",
            name="image",
            field=models.CharField(max_length=255, verbose_name="image"),
        ),
        migrations.AlterField(
            model_name="tourguide_reg",
            name="adhar_card",
            field=models.CharField(
                default="0", max_length=255, null=True, verbose_name="addhar_card"
            ),
        ),
        migrations.AlterField(
            model_name="tourguide_reg",
            name="licence_doc",
            field=models.CharField(
                default="0", max_length=255, null=True, verbose_name="licence_doc"
            ),
        ),
        migrations.AlterField(
            model_name="tourguide_reg",
            name="picture",
            field=models.CharField(
                default="0", max_length=255, null=True, verbose_name="picture"
            ),
        ),
        migrations.AlterField(
            model_name="user_register",
            name="image",
            field=models.CharField(
                default="0", max_length=255, null=True, verbose_name="image"
            ),
        ),
    ]
