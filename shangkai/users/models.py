from datetime import datetime
from django.db import models
from django.utils import timezone

# def post_upload_path(instance,filename):
#     return "media/".format(instance.id,filename)
# upload_to=post_upload_path

from clients.models import (
#    Reg_Hotel,
#    Room_Register,
   Cabs_Reg,
   Driver_Reg,
)

class Normal_UserReg(models.Model):
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user_id = models.CharField("user_id", null=True, max_length=255)
    user_ip = models.CharField("user_ip", null=True, max_length=255)
    name = models.CharField("name", null=True, max_length=255)
    email = models.EmailField("email", null=True, max_length=255)
    mobile = models.CharField("mobile", null=True, max_length=255)
    password = models.CharField("password", null=True, max_length=255)
    image = models.FileField(
        "image", null=True,upload_to="users/", default="users/user_avatar.jpg", max_length=255
    )
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Registration",
            "Registration",
        )


# class User_Hotel_Booking(models.Model):
#     datetime = models.DateTimeField("Created At", auto_now_add=True)
#     user = models.ForeignKey(
#         "users.Normal_UserReg",
#         on_delete=models.CASCADE,
#         default=None,
#         db_constraint=False,
#     )
#     user_ip = models.CharField("user_ip", null=True, max_length=255)
#     hotel_id = models.ForeignKey(
#         "clients.Reg_Hotel",
#         on_delete=models.CASCADE,
#         default=None,
#         db_constraint=False,
#     )
#     room_id = models.ForeignKey(
#         "clients.Room_Register",on_delete=models.CASCADE,
#         default=None,
#         db_constraint=False,
#     )
#     hotel_bookid = models.CharField("hotel_bookid", null=True,default="0", max_length=255)
#     check_in_date = models.CharField("check_in_date", null=True,default="0",  max_length=255)
#     check_in_time = models.CharField("check_in_time", null=True, default="0", max_length=255)
#     check_out_date = models.CharField("check_out_date", null=True,default="0",  max_length=255)
#     check_out_time = models.CharField("check_out_time", null=True,default="0",  max_length=255)
#     guest_no = models.CharField("guests", null=True,default="0", max_length=255)
#     rooms = models.CharField("rooms", null=True,default="0", max_length=255)
#     amount_booking = models.CharField("amount_booking", null=True,default="0", max_length=255)
#     booking_status = models.CharField("status", null=True, default="0", max_length=255)

#     class Meta:
#         verbose_name, verbose_name_plural = (
#             "Hotel Booking",
#             "Hotel Booking",
#         )

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
    cab_bookid = models.CharField("cab_bookid", null=True,default="0", max_length=255)
    check_in_date = models.CharField("check_in_date", null=True,default="0",  max_length=255)
    check_in_time = models.CharField("check_in_time", null=True, default="0", max_length=255)
    check_out_date = models.CharField("check_out_date", null=True,default="0",  max_length=255)
    check_out_time = models.CharField("check_out_time", null=True,default="0",  max_length=255)
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