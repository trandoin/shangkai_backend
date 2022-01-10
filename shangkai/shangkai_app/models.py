from datetime import datetime
from django.db import models
from django.utils import timezone

from users.models import (
    Normal_UserReg,
)


class About_Us(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    about_us = models.TextField("about_us", null=True, max_length=1000)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "About Us",
            "About Us",
        )


class Footer_Copyright(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    footer = models.TextField("footer", null=True, max_length=1000)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Footer",
            "Footer",
        )


class Hotspot_Category(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    title = models.CharField("title", null=True, max_length=1000)
    sub_title = models.CharField("sub_title", null=True, max_length=1000)
    tagline = models.TextField("tagline", null=True, max_length=1000)
    rating = models.CharField("rating", null=True, max_length=1000)
    images = models.CharField("images",default="0", max_length=25500)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Hotspot Category",
            "Hotspot Category",
        )


class Hotel_Category(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    title = models.CharField("title", null=True, max_length=1000)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Hotel Category",
            "Hotel Category",
        )


class Hot_Spots(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    title = models.CharField("title", null=True, max_length=255)
    sub_title = models.CharField("sub_title", null=True, max_length=255)
    city = models.CharField("city", null=True, max_length=255)
    state = models.CharField("state", null=True, max_length=255)
    pin_code = models.CharField("pin_code", null=True, max_length=255)
    geo_location = models.CharField("geo_location", null=True, max_length=255)
    amenites = models.CharField("amenites", null=True, max_length=255)
    history = models.CharField("history", null=True, max_length=255)
    about = models.TextField("about", null=True, max_length=2000)
    images = models.CharField("images",default="0", max_length=25500)
    entry_fee = models.CharField("entry_fee", null=True, max_length=2000)
    parking_fee = models.CharField("parking_fee", null=True, max_length=2000)
    category = models.ForeignKey(
        "shangkai_app.Hotspot_Category", on_delete=models.CASCADE, default=None
    )
    rating = models.CharField("rating", null=True, max_length=2000)
    tags = models.TextField("tags", null=True, max_length=2000)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Hotspots",
            "Hotspots",
        )


class My_Trips(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    title = models.CharField("title", null=True, max_length=255)
    sub_title = models.CharField("sub_title", null=True, max_length=255)
    CATEGORY_CHOICES = (
        ("General", "General"),
        ("Schools/Colleges", "Schools/Colleges"),
        ("Research", "Research"),
    )
    category = models.CharField(
        "Category",
        max_length=150,
        choices=CATEGORY_CHOICES,
        null=True,
        blank=True,
        default="General",
    )
    price = models.CharField("price", null=True, max_length=255)
    description = models.TextField("description", null=True, max_length=255)
    services = models.TextField("services", null=True, max_length=255)
    hotspots_id = models.CharField("hotspots", null=True, max_length=255)
    includes = models.TextField("includes", null=True, max_length=255)
    rules = models.TextField("rules", null=True, max_length=255)
    days_no = models.TextField("days_no", null=True, max_length=2000)
    start_trip = models.DateField("start_trip",default="2021-03-09", null=True, max_length=2000)
    images = models.CharField("images", null=True, default="0", max_length=25500)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "My Trips",
            "My Trips",
        )


class My_Trips_Days(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    my_trip = models.ForeignKey(
        "shangkai_app.My_Trips", on_delete=models.CASCADE, default=None
    )
    description = models.TextField("description", null=True, max_length=255)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "My Trips days",
            "My Trips Days",
        )


class Comments_All(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg", on_delete=models.CASCADE, default=None
    )
    post_id = models.CharField("post_id", null=True, max_length=255)
    comments = models.CharField("comments", null=True, max_length=2000)
    comment_type = models.CharField("comment_type", null=True, max_length=255)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Comments",
            "Comments",
        )


# payment transaction


class Payment_Transaction(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user_id = models.CharField("user_id", null=True, max_length=255)
    transaction_id = models.CharField("transaction_id", null=True, max_length=255)
    transaction_type_id = models.CharField(
        "transaction_type_id", null=True, max_length=2000
    )
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Payment Transaction",
            "Payment Transaction",
        )
