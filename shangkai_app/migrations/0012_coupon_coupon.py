# Generated by Django 4.1.1 on 2022-10-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shangkai_app", "0011_coupon"),
    ]

    operations = [
        migrations.AddField(
            model_name="coupon",
            name="coupon",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
