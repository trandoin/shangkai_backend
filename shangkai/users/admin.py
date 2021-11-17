from django.contrib import admin
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.utils.timezone import utc
from .models import (
    Account_Details,
    Cab_Booking,
    Hotel_Booking,
    Normal_UserReg,
    # Cab_Booking,
    # User_Booking,
)

# Register your models here.


class NormalUserReg(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
        "user_ip",
        "name",
        "email",
        "mobile",
        "password",
        "image",
    ]


admin.site.register(Normal_UserReg, NormalUserReg)

class BookingHotel(admin.ModelAdmin):
    list_display = ["id","user","user_ip","hotel_id","hotel_bookid","check_in_date","check_in_time","check_out_date","check_out_time","guest_no","rooms","amount_booking"]


admin.site.register(Hotel_Booking, BookingHotel)

class CabBooking(admin.ModelAdmin):
    list_display = ["id","user","user_ip","car_id","driver_id","cab_bookid","check_in_date","check_in_time","check_out_date","check_out_time","start_from","end_trip","distance","amount_booking","no_guests"]


admin.site.register(Cab_Booking, CabBooking)

class AccountDetails(admin.ModelAdmin):
    list_display = ["id", "user", "acc_holder", "account_no","bannk_name","bank_branch","ifsc_code","bank_state","pan_card"]


admin.site.register(Account_Details, AccountDetails)