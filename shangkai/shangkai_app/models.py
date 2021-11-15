from datetime import datetime
from django.db import models


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