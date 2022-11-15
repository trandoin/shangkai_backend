# Generated by Django 4.1.1 on 2022-11-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0007_alter_cabs_reg_car_images_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tour_packages",
            name="location_ids",
            field=models.ManyToManyField(
                blank=True, related_name="packages", to="clients.tour_locations"
            ),
        ),
        migrations.AlterField(
            model_name="tourguide_reg",
            name="packages",
            field=models.ManyToManyField(
                blank=True, related_name="guides", to="clients.tour_packages"
            ),
        ),
    ]
