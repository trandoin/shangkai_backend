from django.contrib import admin
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.utils.timezone import utc
from .models import (
    About_Us,
    Comments_All,
    Footer_Copyright,
    Hot_Spots,
    Hotspot_Category,
    Payment_Transaction,
)

#Register your models here.


class AboutUs(admin.ModelAdmin):
    list_display = ["id","about_us"]


admin.site.register(About_Us, AboutUs)

class FooterCopyright(admin.ModelAdmin):
    list_display = ["id","footer"]


admin.site.register(Footer_Copyright, FooterCopyright)

class HotspotCategory(admin.ModelAdmin):
    list_display = ["id","title"]


admin.site.register(Hotspot_Category, HotspotCategory)

class HotSpots(admin.ModelAdmin):
    list_display = ["id","title","sub_title","city","state","pin_code","geo_location","amenites","history","about","images","entry_fee","parking_fee","category","rating","tags"]


admin.site.register(Hot_Spots,HotSpots)

class CommentsAll(admin.ModelAdmin):
    list_display = ["id","user","post_id","comments","comment_type"]


admin.site.register(Comments_All,CommentsAll)

class PaymentTransaction(admin.ModelAdmin):
    list_display = ["id","user_id","transaction_id","transaction_type_id"]


admin.site.register(Payment_Transaction,PaymentTransaction)