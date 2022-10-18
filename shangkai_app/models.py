from datetime import datetime
from email.policy import default
from django.db import models
from django.utils import timezone
import uuid

from users.models import (
    Normal_UserReg,
)

from clients.models import (
    User_Register,
)


class About_Us(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    about_us = models.TextField("about_us", null=True, max_length=1000)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "About Us",
            "About Us",
        )


class Footer_Copyright(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    footer = models.TextField("footer", null=True, max_length=1000)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Footer",
            "Footer",
        )


class Contact_Us(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    name = models.CharField("Name", null=True, max_length=255)
    email = models.EmailField("Email", null=True, max_length=255)
    mobile_num = models.CharField("Mobile No", null=True, max_length=255)
    message = models.TextField("Message", null=True, max_length=1000)
    status = models.CharField("Status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Contact Us",
            "Contact Us",
        )


class Hotspot_Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    title = models.CharField("title", null=True, max_length=1000)
    sub_title = models.CharField("sub_title", null=True, max_length=1000)
    tagline = models.TextField("tagline", null=True, max_length=1000)
    rating = models.CharField("rating", null=True, max_length=1000)
    images = models.CharField("images", default="0", max_length=25500)
    # is_recommended = models.CharField("is_recommended", null=True, default="0", max_length=255)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Hotspot Category",
            "Hotspot Category",
        )

    def __str__(self):
        return str(self.title)


class Hotel_Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    title = models.CharField("title", null=True, max_length=1000)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Hotel Category",
            "Hotel Category",
        )

    def __str__(self):
        return str(self.title)


class Hot_Spots(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    title = models.CharField("title", null=True, max_length=255)
    sub_title = models.CharField("sub_title", null=True, max_length=255)
    city = models.CharField("city", null=True, max_length=255)
    state = models.CharField("state", null=True, max_length=255)
    pin_code = models.CharField("pin_code", null=True, max_length=255)
    geo_location = models.CharField("geo_location", null=True, max_length=255)
    amenites = models.CharField("amenites", null=True, max_length=255)
    history = models.CharField("history", null=True, max_length=255)
    about = models.TextField("about", null=True, max_length=2000)
    para1 = models.TextField("para1", null=True, max_length=2000)
    para2 = models.TextField("para2", null=True, max_length=2000)
    para3 = models.TextField("para3", null=True, max_length=2000)
    transport = models.CharField("transport", null=True, max_length=255)
    title_image = models.ImageField("title_image", upload_to="hotspot_images",null=True)
    images = models.CharField("images", default="0", max_length=25500)
    entry_fee = models.CharField("entry_fee", null=True, max_length=2000)
    parking_fee = models.CharField("parking_fee", null=True, max_length=2000)
    category = models.ForeignKey(
        "shangkai_app.Hotspot_Category", on_delete=models.CASCADE, default=None
    )
    rating = models.CharField("rating", null=True, max_length=2000)
    tags = models.TextField("tags", null=True, max_length=2000)
    # is_recommended = models.CharField("is_recommended", null=True, default="0", max_length=255)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Hotspots",
            "Hotspots",
        )

    def __str__(self):
        return str(self.title)

class HotSpot_Images(models.Model):
    image = models.ImageField("image", upload_to="hotspot_images", null=True, blank=True)
    hotspot = models.ForeignKey(
        "shangkai_app.Hot_Spots", on_delete=models.CASCADE, related_name="hotspot_images"
    )
    class Meta:
        verbose_name, verbose_name_plural = (
            "Hotspot Images",
            "Hotspot Images",
        )

class Tracking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("title", null=True, max_length=255)
    start_date = models.DateTimeField("Starting on")
    booking_start = models.DateTimeField("Booking on")
    booking_upto = models.DateTimeField("Booking upto")
    seats = models.IntegerField("seats",)
    booked = models.IntegerField("booked", default=0)
    amount = models.CharField("amount a", null=True, max_length=255)
    amount2 = models.CharField("amount b", null=True, max_length=255)
    student_amount = models.CharField("student amount a", null=True, max_length=255)
    student_amount2 = models.CharField("student amount b", null=True, max_length=255)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Tracking",
            "Tracking",
        )
    def __str__(self):
        return self.title
class Tracking_Order(models.Model):
    id = models.CharField("id", primary_key=True, max_length=255)
    seats = models.CharField("seats",max_length=255)
    is_stay = models.BooleanField("is_stay", default=False)
    is_student = models.BooleanField("is_student", default=False)
    currency = models.CharField("currency", max_length=3)
    amount = models.CharField("amount", max_length=255)
    tracking = models.ForeignKey(
        "shangkai_app.Tracking", on_delete=models.CASCADE, default=None
    )
    
class Tracking_Bookings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tracking = models.ForeignKey(
        "shangkai_app.Tracking", on_delete=models.CASCADE, default=None
    )
    user = models.ForeignKey(
        "users.Normal_UserReg", on_delete=models.CASCADE, default=None
    )
    payment_id = models.CharField("payment_id", null=True, max_length=255)
    order_id = models.CharField("order_id", null=True, max_length=255)
    signature = models.CharField("signature", null=True, max_length=255)
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    seats = models.IntegerField()
    amount = models.CharField("amount", null=True, max_length=255)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Tracking Bookings",
            "Tracking Bookings",
        )
    def __str__(self):
        return str(self.id)

class My_Trips(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    title = models.CharField("title", null=True, max_length=255)
    sub_title = models.CharField("sub_title", null=True, max_length=255)
    CATEGORY_CHOICES = (
        ("General", "General"),
        ("Schools/Colleges", "Schools/Colleges"),
        ("Research", "Research"),
    )
    category = models.CharField(
        "Category",
        max_length=150,
        choices=CATEGORY_CHOICES,
        null=True,
        blank=True,
        default="General",
    )
    price = models.CharField("Price", null=True, max_length=255)
    offer_price = models.CharField("Offer Price", null=True, max_length=255)
    special_offer = models.CharField(
        "Special Offer", null=True, default="0", max_length=255
    )
    deadline_date = models.CharField("Deadline Date", null=True, max_length=255)
    exlusion = models.TextField("Exlusion", null=True, max_length=2550)
    description = models.TextField("description", null=True, max_length=255)
    services = models.TextField("services", null=True, max_length=255)
    hotspots_id = models.CharField("hotspots", null=True, max_length=255)
    includes = models.TextField("includes", null=True, max_length=255)
    rules = models.TextField("rules", null=True, max_length=255)
    days_no = models.CharField("days_no", null=True, max_length=2000)
    start_trip = models.DateField(
        "start_trip", default="2021-03-09", null=True, max_length=2000
    )
    images = models.CharField("images", null=True, default="0", max_length=25500)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "My Trips",
            "My Trips",
        )

    def __str__(self):
        return str(self.title)


class My_Trips_Days(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    my_trip = models.ForeignKey(
        "shangkai_app.My_Trips", on_delete=models.CASCADE, default=None, related_name="trip_days"
    )
    description = models.TextField("description", null=True, max_length=255)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "My Trips days",
            "My Trips Days",
        )


class Admin_Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime = models.CharField("Created At", null=True, max_length=255)
    title = models.CharField("Title", null=True, max_length=255)
    message = models.TextField("Message", null=True, max_length=255)
    status = models.CharField("Status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Admin_Notification",
            "Admin_Notification",
        )


class Blog_Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "clients.User_Register", on_delete=models.CASCADE, default=None
    )
    title = models.CharField("Category Title", null=True, max_length=255)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Blog Category",
            "Blog Category",
        )

    def __str__(self):
        return str(self.title)


class Blog_Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "clients.User_Register", on_delete=models.CASCADE, default=None
    )
    category = models.ForeignKey(
        "shangkai_app.Blog_Category", on_delete=models.CASCADE, default=None
    )
    title = models.CharField("Post Title", null=True, max_length=555)
    text = models.TextField("Post Text", null=True, max_length=2000)
    feature_image = models.CharField("Feature Image", null=True, max_length=2000)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Blog Posts",
            "Blog Posts",
        )

    def __str__(self):
        return str(self.title)


class BlogPost_Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    post = models.ForeignKey(
        "shangkai_app.Blog_Post", on_delete=models.CASCADE, default=None
    )
    user_ip = models.CharField("User IP", null=True, max_length=255)
    name = models.CharField("Name", null=True, max_length=255)
    email = models.EmailField("Email", null=True, max_length=255)
    comments = models.TextField("Comment", null=True, max_length=2000)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Blog Post Comments",
            "Blog Post Comments",
        )


class Comments_All(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(
        "users.Normal_UserReg", on_delete=models.CASCADE, default=None
    )
    post_id = models.CharField("post_id", null=True, max_length=255)
    comments = models.CharField("comments", null=True, max_length=2000)
    comment_type = models.CharField("comment_type", null=True, max_length=255)
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Comments",
            "Comments",
        )


# payment transaction


class Payment_Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datetime = models.DateTimeField("Created At", auto_now_add=True)
    user_id = models.CharField("user_id", null=True, max_length=255)
    transaction_id = models.CharField("transaction_id", null=True, max_length=255)
    transaction_type_id = models.CharField(
        "transaction_type_id", null=True, max_length=2000
    )
    status = models.CharField("status", null=True, default="0", max_length=255)

    class Meta:
        verbose_name, verbose_name_plural = (
            "Payment Transaction",
            "Payment Transaction",
        )
