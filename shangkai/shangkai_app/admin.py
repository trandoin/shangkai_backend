from django.contrib import admin
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.utils.timezone import utc
from .models import (
    About_Us,
    Footer_Copyright,
)

# Register your models here.


class AboutUs(admin.ModelAdmin):
    list_display = ["id","about_us"]


admin.site.register(About_Us, AboutUs)

class FooterCopyright(admin.ModelAdmin):
    list_display = ["id","footer"]


admin.site.register(Footer_Copyright, FooterCopyright)