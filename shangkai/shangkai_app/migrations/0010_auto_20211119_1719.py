# Generated by Django 3.2.7 on 2021-11-19 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shangkai_app", "0009_auto_20211117_1853"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hot_spots",
            name="rating",
        ),
        migrations.AddField(
            model_name="hot_spots",
            name="rating",
            field=models.CharField(max_length=2000, null=True, verbose_name="rating"),
        ),
    ]
