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
    User_Hotspots_Bookings,
    User_Trip_Cart,
    User_Cab_Payment,
    User_Trip_Booking,
    User_Trips_Payment,
    User_Guide_Booking,
    User_Hotspots_Cart,
    User_Ratings,
)


##################### """"""""" ACCOUNTS DETAILS """""""""""" ########################


class NormalUserReg(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
        "user_ip",
        "name",
        "email",
        "mobile",
        "password",
        "otp",
        "image",
    ]


admin.site.register(Normal_UserReg, NormalUserReg)


class UserRatings(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "cleaness",
        "hospitility",
        "location",
        "aesthetic",
        "value",
        "scenic_beauty",
        "surrounding",
        "safety_security",
        "item_id",
        "item_type",
        "message",
        "status",
    ]


admin.site.register(User_Ratings, UserRatings)


class AccountDetails(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "acc_holder",
        "account_no",
        "bannk_name",
        "bank_branch",
        "ifsc_code",
        "bank_state",
        "pan_card",
    ]


admin.site.register(User_Account_Details, AccountDetails)

##################### """"""""" HOTELS """""""""""" ########################


class HotelCart(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "hotel_id",
        "check_in_date",
        "check_in_time",
        "check_out_date",
        "check_out_time",
        "guest_no",
        "rooms",
        "amount_booking",
    ]


admin.site.register(User_Hotel_Cart, HotelCart)


class BookingHotel(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "user_ip",
        "hotel_id",
        "hotel_bookid",
        "check_in_date",
        "check_in_time",
        "check_out_date",
        "check_out_time",
        "guest_no",
        "rooms",
        "amount_booking",
        "razorpay_id",
        "booking_status",
    ]


admin.site.register(User_Hotel_Booking, BookingHotel)


class UserHotelPayment(admin.ModelAdmin):
    list_display = ["id", "user", "hotel_booking", "payment_id", "payment_status"]


admin.site.register(User_Hotel_Payment, UserHotelPayment)

##################### """"""""" CABS """""""""""" ########################


class UserCabCart(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "car_id",
        "driver_id",
        "check_in_date",
        "check_in_time",
        "check_out_date",
        "check_out_time",
        "start_from",
        "end_trip",
        "distance",
        "amount_booking",
        "no_guests",
    ]


admin.site.register(User_Cab_Cart, UserCabCart)


class CabBooking(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "user_ip",
        "car_id",
        "driver_id",
        "cab_bookid",
        "check_in_date",
        "check_in_time",
        "check_out_date",
        "check_out_time",
        "start_from",
        "end_trip",
        "distance",
        "amount_booking",
        "no_guests",
        "razorpay_id",
        "booking_status",
    ]


admin.site.register(User_Cab_Booking, CabBooking)


class UserCabbookingPayment(admin.ModelAdmin):
    list_display = ["id", "user", "cab_booking", "payment_id"]


admin.site.register(User_Cab_Payment, UserCabbookingPayment)


##################### """"""""" TRIPS """""""""""" ########################


class UserTripCart(admin.ModelAdmin):
    list_display = ["id", "user", "trip_id", "no_guests"]


admin.site.register(User_Trip_Cart, UserTripCart)


class UserTripBooking(admin.ModelAdmin):
    list_display = ["id", "user", "trip_id", "trip_ammount", "no_guests","trip_ammount","razorpay_id","trip_cart_status"]


admin.site.register(User_Trip_Booking, UserTripBooking)


class UserTripsPayment(admin.ModelAdmin):
    list_display = ["id", "user", "trip_booking", "payment_id"]


admin.site.register(User_Trips_Payment, UserTripsPayment)


class UserGuideBooking(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "client_id",
        "guide_id",
        "no_guests",
        "booking_date",
        "guide_amount",
        "razorpay_id",
        "status",
    ]


admin.site.register(User_Guide_Booking, UserGuideBooking)


class UserHotspotsCart(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "hostpots_id",
        "no_guests",
        "booking_date",
        "cart_amount",
    ]


admin.site.register(User_Hotspots_Cart, UserHotspotsCart)


class UserHotspotsBookings(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "cart_id",
        "no_guests",
        "booking_date",
        "booking_amount",
        "razorpay_id",
    ]


admin.site.register(User_Hotspots_Bookings, UserHotspotsBookings)
