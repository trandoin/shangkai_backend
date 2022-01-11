from datetime import datetime
from django.db import models
from django.utils import timezone
import random

# def post_upload_path(instance,filename):
#     return "media/".format(instance.id,filename)
# upload_to=post_upload_path

from clients.models import (
    Cabs_Reg,
    Reg_Hotel,
    Room_Register,
    Driver_Reg,
    User_Register,
    TourGuide_Reg,
    Tour_Packages,
    Tour_locations,
)

# from shangkai_app.models import (
#     Hotspot_Category,
#     Hot_Spots,
# )


##################### """"""""" ACCOUNTS DETAILS """""""""""" ########################


class Normal_UserReg(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user_id = models.CharField("user_id", null=True, max_length=255)
    user_ip = models.CharField("user_ip", null=True, max_length=255)
    name = models.CharField("name", null=True, max_length=255)
    email = models.EmailField("email", null=True, max_length=255, unique=True)
    mobile = models.CharField("mobile", null=True, max_length=255)
    password = models.CharField("password", null=True, max_length=255)
    otp = models.CharField("otp", null=True, max_length=255)
    image = models.FileField("image", default="0", null=True, max_length=255)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Registration",
            "Registration",
        )

    def __str__(self):
        return self.name


class User_Account_Details(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    acc_holder = models.CharField("acc_holder", null=True, max_length=255)
    account_no = models.CharField("account_no", null=True, max_length=255)
    bannk_name = models.CharField("bannk_name", null=True, max_length=255)
    bank_branch = models.CharField("bank_branch", null=True, max_length=255)
    ifsc_code = models.CharField("ifsc_code", null=True, max_length=255)
    bank_state = models.CharField("bank_state", null=True, max_length=255)
    pan_card = models.CharField("pan_card", null=True, max_length=255)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Bank Details",
            "Bank Details",
        )


##################### """"""""" HOTELS """""""""""" ########################


class User_Hotel_Cart(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    hotel_id = models.ForeignKey(
        "clients.Reg_Hotel",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    room_id = models.ForeignKey(
        "clients.Room_Register",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    check_in_date = models.CharField(
        "check_in_date", null=True, default="0", max_length=255
    )
    check_in_time = models.CharField(
        "check_in_time", null=True, default="0", max_length=255
    )
    check_out_date = models.CharField(
        "check_out_date", null=True, default="0", max_length=255
    )
    check_out_time = models.CharField(
        "check_out_time", null=True, default="0", max_length=255
    )
    guest_no = models.CharField("guests", null=True, default="0", max_length=255)
    rooms = models.CharField("rooms", null=True, default="0", max_length=255)
    amount_booking = models.CharField(
        "amount_booking", null=True, default="0", max_length=255
    )
    booking_status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Hotel Cart",
            "Hotel Cart",
        )


class User_Hotel_Booking(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    user_ip = models.CharField("user_ip", null=True, max_length=255)
    hotel_id = models.ForeignKey(
        "clients.Reg_Hotel",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    room_id = models.ForeignKey(
        "clients.Room_Register",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    hotel_bookid = models.CharField(
        "hotel_bookid", null=True, default="0", max_length=255
    )
    check_in_date = models.CharField(
        "check_in_date", null=True, default="0", max_length=255
    )
    check_in_time = models.CharField(
        "check_in_time", null=True, default="0", max_length=255
    )
    check_out_date = models.CharField(
        "check_out_date", null=True, default="0", max_length=255
    )
    check_out_time = models.CharField(
        "check_out_time", null=True, default="0", max_length=255
    )
    guest_no = models.CharField("guests", null=True, default="0", max_length=255)
    rooms = models.CharField("rooms", null=True, default="0", max_length=255)
    amount_booking = models.CharField(
        "amount_booking", null=True, default="0", max_length=255
    )
    booking_status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Hotel Booking",
            "Hotel Booking",
        )


class User_Hotel_Payment(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    hotel_booking = models.ForeignKey(
        "users.User_Hotel_Booking",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    payment_id = models.CharField("payment_id", null=True, max_length=255)
    payment_status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "User Hotel Payments",
            "User Hotel Payments",
        )


##################### """"""""" CABS """""""""""" ########################


class User_Cab_Cart(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    car_id = models.ForeignKey(
        "clients.Cabs_Reg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    driver_id = models.ForeignKey(
        "clients.Driver_Reg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    check_in_date = models.CharField(
        "check_in_date", null=True, default="0", max_length=255
    )
    check_in_time = models.CharField(
        "check_in_time", null=True, default="0", max_length=255
    )
    check_out_date = models.CharField(
        "check_out_date", null=True, default="0", max_length=255
    )
    check_out_time = models.CharField(
        "check_out_time", null=True, default="0", max_length=255
    )
    start_from = models.CharField("start_from", null=True, max_length=255)
    end_trip = models.CharField("end_trip", null=True, max_length=255)
    distance = models.CharField("distance", null=True, max_length=255)
    amount_booking = models.CharField("amount", null=True, max_length=255)
    no_guests = models.CharField("no_guests", null=True, max_length=255)
    booking_status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Cab Cart",
            "Cab Cart",
        )


class User_Cab_Booking(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    user_ip = models.CharField("user_ip", null=True, max_length=255)
    car_id = models.ForeignKey(
        "clients.Cabs_Reg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    driver_id = models.ForeignKey(
        "clients.Driver_Reg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    cab_bookid = models.CharField("cab_bookid", null=True, default="0", max_length=255)
    check_in_date = models.CharField(
        "check_in_date", null=True, default="0", max_length=255
    )
    check_in_time = models.CharField(
        "check_in_time", null=True, default="0", max_length=255
    )
    check_out_date = models.CharField(
        "check_out_date", null=True, default="0", max_length=255
    )
    check_out_time = models.CharField(
        "check_out_time", null=True, default="0", max_length=255
    )
    start_from = models.CharField("start_from", null=True, max_length=255)
    end_trip = models.CharField("end_trip", null=True, max_length=255)
    distance = models.CharField("distance", null=True, max_length=255)
    amount_booking = models.CharField("amount", null=True, max_length=255)
    no_guests = models.CharField("no_guests", null=True, max_length=255)
    booking_status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Cab Booking",
            "Cab Booking",
        )


class User_Cab_Payment(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    cab_booking = models.ForeignKey(
        "users.User_Cab_Booking",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    payment_id = models.CharField("payment_id", null=True, max_length=255)
    payment_status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "User Cab Payments",
            "User Cab Payments",
        )


##################### """"""""" TRIPS """""""""""" ########################


class User_Trip_Cart(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    trip_id = models.ForeignKey(
        "shangkai_app.My_Trips",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    no_guests = models.CharField("no_guests", null=True, max_length=255)
    trip_cart_status = models.CharField(
        "status", null=True, default="0", max_length=255
    )

    class Meta:
        verbose_name, verbose_name_plural = (
            "Trip Carts",
            "Trip Carts",
        )


class User_Trip_Booking(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    trip_id = models.ForeignKey(
        "shangkai_app.My_Trips",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    no_guests = models.CharField("no_guests", null=True, max_length=255)
    trip_ammount = models.CharField("trip_ammount", null=True, max_length=255)
    trip_cart_status = models.CharField(
        "status", null=True, default="0", max_length=255
    )

    class Meta:
        verbose_name, verbose_name_plural = (
            "Trip Booking",
            "Trip Booking",
        )


class User_Trips_Payment(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    trip_booking = models.ForeignKey(
        "users.User_Trip_Booking",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    payment_id = models.CharField("payment_id", null=True, max_length=255)
    payment_status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "User Trips Payments",
            "User Trips Payments",
        )


class User_Guide_Booking(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    client_id = models.ForeignKey(
        "clients.User_Register",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    guide_id = models.ForeignKey(
        "clients.TourGuide_Reg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    no_guests = models.CharField("no_guests", null=True, max_length=255)
    booking_date = models.DateField(
        "booking_date", default="2021-03-09", null=True, max_length=255
    )
    guide_amount = models.CharField("guide_ammount", null=True, max_length=255)
    razorpay_id = models.CharField(
        "razorpay_id", null=True, default="0", max_length=255
    )
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Tour Guide Booking",
            "Tour Guide Booking",
        )


class User_Hotspots_Cart(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    hostpots_id = models.ForeignKey(
        "shangkai_app.Hot_Spots",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    no_guests = models.CharField("no_guests", null=True, max_length=255)
    booking_date = models.DateField(
        "booking_date", default="2021-03-09", null=True, max_length=255
    )
    cart_amount = models.CharField("cart_ammount", null=True, max_length=255)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Hotspots Cart",
            "Hotspots Cart",
        )


class User_Hotspots_Bookings(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    cart_id = models.ForeignKey(
        "users.User_Hotspots_Cart",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    no_guests = models.CharField("no_guests", null=True, max_length=255)
    booking_date = models.DateField(
        "booking_date", default="2021-03-09", null=True, max_length=255
    )
    booking_amount = models.CharField("booking_amount", null=True, max_length=255)
    razorpay_id = models.CharField(
        "razorpay_id", null=True, default="0", max_length=255
    )
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Hotspots Bookings",
            "Hotspots Bookings",
        )
