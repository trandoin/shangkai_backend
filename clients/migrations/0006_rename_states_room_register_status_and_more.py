# Generated by Django 4.1.1 on 2022-11-11 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0005_reg_hotel_title_image_room_register_title_image_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="room_register",
            old_name="states",
            new_name="status",
        ),
        migrations.AlterField(
            model_name="hotelimages",
            name="hotel",
            field=models.ForeignKey(
                db_constraint=False,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="gallery_images",
                to="clients.reg_hotel",
            ),
        ),
        migrations.AlterField(
            model_name="roomimages",
            name="room",
            field=models.ForeignKey(
                db_constraint=False,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="gallery_images",
                to="clients.room_register",
            ),
        ),
    ]