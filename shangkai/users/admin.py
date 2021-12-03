from datetime import datetime
from django.db import models
from django.contrib import admin
from django.utils import timezone
from .models import (
    User_Account_Details,
    User_Cab_Booking,
    User_Hotel_Booking,
    Normal_UserReg,
    User_Hotel_Cart,
    User_Cab_Cart,
    User_Hotel_Payment,
    User_Trip_Cart,
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


admin.site.register(User_Hotel_Booking, BookingHotel)

class HotelCart(admin.ModelAdmin):
    list_display = ["id","user","hotel_id","check_in_date","check_in_time","check_out_date","check_out_time","guest_no","rooms","amount_booking"]


admin.site.register(User_Hotel_Cart, HotelCart)

class CabBooking(admin.ModelAdmin):
    list_display = ["id","user","user_ip","car_id","driver_id","cab_bookid","check_in_date","check_in_time","check_out_date","check_out_time","start_from","end_trip","distance","amount_booking","no_guests"]


admin.site.register(User_Cab_Booking, CabBooking)

class UserHotelPayment(admin.ModelAdmin):
    list_display = ["id","user","hotel_booking","payment_id","payment_status"]


admin.site.register(User_Hotel_Payment, UserHotelPayment)

class AccountDetails(admin.ModelAdmin):
    list_display = ["id", "user", "acc_holder", "account_no","bannk_name","bank_branch","ifsc_code","bank_state","pan_card"]


admin.site.register(User_Account_Details, AccountDetails)

class UserCabCart(admin.ModelAdmin):
    list_display = ["id", "user", "car_id", "driver_id","check_in_date","check_in_time","check_out_date","check_out_time","start_from","end_trip","distance","amount_booking","no_guests"]


admin.site.register(User_Cab_Cart, UserCabCart)


class UserTripCart(admin.ModelAdmin):
    list_display = ["id", "user", "trip_id", "no_guests"]


admin.site.register(User_Trip_Cart, UserTripCart)
