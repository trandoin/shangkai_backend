from django.contrib import admin
from django.contrib import admin
from django.contrib.admin.sites import AdminSite

# from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.utils.timezone import utc
from .models import (
    About_Us,
    Comments_All,
    Footer_Copyright,
    Hot_Spots,
    HotSpot_Images,
    Hotspot_Category,
    Payment_Transaction,
    Hotel_Category,
    My_Trips,
    My_Trips_Days,
    Blog_Category,
    Blog_Post,
    BlogPost_Comments,
    Admin_Notification,
    Contact_Us,
    Tracking,
)

# Register your models here.


class AboutUs(admin.ModelAdmin):
    list_display = ["id", "about_us"]


admin.site.register(About_Us, AboutUs)


class FooterCopyright(admin.ModelAdmin):
    list_display = ["id", "footer"]


admin.site.register(Footer_Copyright, FooterCopyright)


class ContactUs(admin.ModelAdmin):
    list_display = ["id", "name", "email", "mobile_num", "message", "status"]


admin.site.register(Contact_Us, ContactUs)


class Notification(admin.ModelAdmin):
    list_display = ["id", "title", "message", "status"]


admin.site.register(Admin_Notification, Notification)


class HotspotCategory(admin.ModelAdmin):
    list_display = ["id", "title", "sub_title", "tagline", "rating", "images"]


admin.site.register(Hotspot_Category, HotspotCategory)


class HotelCategory(admin.ModelAdmin):
    list_display = ["id", "title"]


admin.site.register(Hotel_Category, HotelCategory)


class HotSpots(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "sub_title",
        "city",
        "state",
        "pin_code",
        "geo_location",
        "amenites",
        "history",
        "about",
        "images",
        "entry_fee",
        "parking_fee",
        "category",
        "rating",
        "tags",
    ]


admin.site.register(Hot_Spots, HotSpots)
admin.site.register(HotSpot_Images)
admin.site.register(Tracking)


class MyTrips(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "sub_title",
        "category",
        "price",
        "description",
        "services",
        "includes",
        "rules",
        "days_no",
        "start_trip",
        "images",
    ]


admin.site.register(My_Trips, MyTrips)


class MyTripDays(admin.ModelAdmin):
    list_display = ["id", "description"]


admin.site.register(My_Trips_Days, MyTripDays)


class CommentsAll(admin.ModelAdmin):
    list_display = ["id", "user", "post_id", "comments", "comment_type"]


admin.site.register(Comments_All, CommentsAll)


class PaymentTransaction(admin.ModelAdmin):
    list_display = ["id", "user_id", "transaction_id", "transaction_type_id"]


admin.site.register(Payment_Transaction, PaymentTransaction)


class BlogCategory(admin.ModelAdmin):
    list_display = ["id", "user", "title"]


admin.site.register(Blog_Category, BlogCategory)


class BlogPosts(admin.ModelAdmin):
    list_display = ["id", "category", "title", "text", "feature_image"]


admin.site.register(Blog_Post, BlogPosts)


class BlogPostComments(admin.ModelAdmin):
    list_display = ["id", "post", "name", "email", "comments"]


admin.site.register(BlogPost_Comments, BlogPostComments)
