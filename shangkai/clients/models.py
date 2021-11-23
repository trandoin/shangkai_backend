from datetime import datetime
from django.db import models
from django.utils import timezone


# from shangkai_app.models import (
#     Hotel_Category,
# )

class User_Register(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user_id = models.CharField("user_id", null=True, max_length=255)
    user_ip = models.CharField("user_ip", null=True, max_length=255)
    name = models.CharField("name", null=True, max_length=255)
    email = models.EmailField("email", null=True, max_length=255)
    mobile = models.CharField("mobile", null=True, max_length=255)
    password = models.CharField("password", null=True, max_length=255)
    user_type = models.CharField("user_type",null=True,default="0", max_length=255)
    image = models.FileField(
        "image", null=True, upload_to="clients/", default="clients/user_avatar.jpg", max_length=255
    )
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Clients Registration",
            "Clients Registration",
        )


class Reg_Hotel(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "clients.User_Register",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    hotel_cat = models.ForeignKey(
        "shangkai_app.Hotel_Category",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    hotel_code = models.CharField("hotel_id", null=True, max_length=255)
    hotel_name = models.CharField("hotel_name", null=True, max_length=255)
    hotel_address = models.TextField("hotel_address", null=True, max_length=1000)
    hotel_city = models.CharField("hotel_city", null=True, max_length=255)
    hotel_state = models.CharField("hotel_state", null=True, max_length=255)
    geo_location = models.CharField("geo_location", null=True, max_length=255)
    pin_code = models.CharField("pincode", null=True, max_length=255)
    room_rates = models.CharField("rates", null=True, max_length=255)
    hotel_facilites = models.TextField("facilites", null=True, max_length=5000)
    max_guests_limit = models.CharField("limits", null=True, max_length=255)
    hotel_images = models.FileField(
        "images", null=True,upload_to="hotels/", default="hotels/hotel_image.jpg", max_length=255
    )
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Hotel Registration",
            "Hotel Registration",
        )


class Room_Register(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "clients.User_Register",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False
    )
    hotel_id = models.ForeignKey(
        "clients.Reg_Hotel",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False
    )
    room_id = models.CharField("room_id", null=True, max_length=255)
    room_type = models.CharField("room_type", null=True, max_length=255)
    bed_type = models.TextField("bed_type", null=True, max_length=1000)
    totel_beds = models.CharField("totel_beds", null=True, max_length=255)
    room_rates = models.CharField("rates", null=True, max_length=255)
    room_facilites = models.TextField("facilites", null=True, max_length=5000)
    max_guests_limit = models.CharField("limits", null=True, max_length=255)
    no_rooms = models.CharField("no_of_rooms", null=True, max_length=255)
    rating = models.CharField("rating", null=True, max_length=255)
    tags = models.TextField("tags", null=True, max_length=255)
    extra_services = models.TextField("extra_services", null=True, max_length=255)
    room_images = models.FileField(
        "images", null=True,upload_to="rooms/", default="rooms/room_image.jpg", max_length=255
    )
    states = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Room Registration",
            "Room Registration",
        )

class Driver_Reg(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "clients.User_Register",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    driver_id = models.CharField("driver_id", null=True, max_length=255)
    driver_name = models.CharField("driver_name", null=True, max_length=255)
    driver_address = models.CharField("driver_address", null=True, max_length=255)
    driver_mobile = models.CharField("driver_mobile", null=True, max_length=255)
    driver_email = models.CharField("driver_email", null=True, max_length=255)
    languages = models.CharField("languages", null=True, max_length=255)
    working_hours = models.CharField("working_hours", null=True, max_length=255)
    licence_no = models.CharField("licence_no", null=True, max_length=255)
    driver_doc = models.FileField(
        "driver_doc", null=True,upload_to="driver_doc/", default="driver_doc/driver_avatar.jpg", max_length=255
    )
    picture = models.FileField(
        "picture", null=True,upload_to="driver_images/", default="driver_images/driver_avatar.jpg", max_length=255
    )
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Car Driver Registration",
            "Car Driver Registration",
        )

class Cabs_Reg(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "clients.User_Register",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    driver = models.ForeignKey(
        "clients.Driver_Reg",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    car_code = models.CharField("car_code", null=True, max_length=255)
    car_name = models.CharField("car_name", null=True, max_length=255)
    car_type = models.CharField("car_type", null=True, max_length=255)
    capacity = models.CharField("capacity", null=True, max_length=255)
    vehicle_no = models.CharField("vehicle_no", null=True, max_length=255)
    car_mou = models.CharField("car_mou", null=True, max_length=255)
    pickup_point = models.CharField("pickup_point", null=True, max_length=255)
    car_rating = models.CharField("car_rating", null=True, max_length=255)
    car_doc = models.FileField(
        "car_doc", null=True,upload_to="car_doc/", default="car_doc/car_doc.jpg", max_length=255
    )
    car_images = models.FileField(
        "car_images", null=True,upload_to="car_images/", default="car_images/car_image.jpg", max_length=255
    )
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Car Registration",
            "Car Registration",
        )

class Account_Details(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "clients.User_Register",
        on_delete=models.CASCADE,
        default=None,
        db_constraint=False,
    )
    acc_holder = models.CharField("acc_holder", null=True, max_length=255)
    account_no = models.CharField("account_no", null=True, max_length=255)
    bannk_name = models.CharField("bannk_name", null=True,  max_length=255)
    bank_branch = models.CharField("bank_branch", null=True, max_length=255)
    ifsc_code = models.CharField("ifsc_code", null=True, max_length=255)
    bank_state = models.CharField("bank_state", null=True,  max_length=255)
    pan_card = models.CharField("pan_card", null=True,  max_length=255)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Bank Details",
            "Bank Details",
        )        