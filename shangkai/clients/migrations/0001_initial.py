# Generated by Django 3.2.7 on 2022-01-10 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account_Details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "datetime",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "acc_holder",
                    models.CharField(
                        max_length=255, null=True, verbose_name="acc_holder"
                    ),
                ),
                (
                    "account_no",
                    models.CharField(
                        max_length=255, null=True, verbose_name="account_no"
                    ),
                ),
                (
                    "bannk_name",
                    models.CharField(
                        max_length=255, null=True, verbose_name="bannk_name"
                    ),
                ),
                (
                    "bank_branch",
                    models.CharField(
                        max_length=255, null=True, verbose_name="bank_branch"
                    ),
                ),
                (
                    "ifsc_code",
                    models.CharField(
                        max_length=255, null=True, verbose_name="ifsc_code"
                    ),
                ),
                (
                    "bank_state",
                    models.CharField(
                        max_length=255, null=True, verbose_name="bank_state"
                    ),
                ),
                (
                    "pan_card",
                    models.CharField(
                        max_length=255, null=True, verbose_name="pan_card"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="status"
                    ),
                ),
            ],
            options={
                "verbose_name": "Bank Details",
                "verbose_name_plural": "Bank Details",
            },
        ),
        migrations.CreateModel(
            name="Cabs_Reg",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "datetime",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "car_code",
                    models.CharField(
                        max_length=255, null=True, verbose_name="car_code"
                    ),
                ),
                (
                    "car_name",
                    models.CharField(
                        max_length=255, null=True, verbose_name="car_name"
                    ),
                ),
                (
                    "car_type",
                    models.CharField(
                        max_length=255, null=True, verbose_name="car_type"
                    ),
                ),
                (
                    "capacity",
                    models.CharField(
                        max_length=255, null=True, verbose_name="capacity"
                    ),
                ),
                (
                    "vehicle_no",
                    models.CharField(
                        max_length=255, null=True, verbose_name="vehicle_no"
                    ),
                ),
                (
                    "car_mou",
                    models.CharField(max_length=255, null=True, verbose_name="car_mou"),
                ),
                (
                    "car_fee",
                    models.CharField(max_length=255, null=True, verbose_name="car_fee"),
                ),
                (
                    "pickup_point",
                    models.CharField(
                        max_length=255, null=True, verbose_name="pickup_point"
                    ),
                ),
                (
                    "destination",
                    models.CharField(
                        max_length=255, null=True, verbose_name="destination"
                    ),
                ),
                (
                    "checkin_date",
                    models.CharField(
                        max_length=255, null=True, verbose_name="checkin_date"
                    ),
                ),
                (
                    "checkout_date",
                    models.CharField(
                        max_length=255, null=True, verbose_name="checkout_date"
                    ),
                ),
                (
                    "car_rating",
                    models.CharField(
                        max_length=255, null=True, verbose_name="car_rating"
                    ),
                ),
                (
                    "car_rc",
                    models.FileField(
                        default="0",
                        max_length=255,
                        null=True,
                        upload_to="",
                        verbose_name="car_rc",
                    ),
                ),
                (
                    "car_insurance",
                    models.FileField(
                        default="0",
                        max_length=255,
                        null=True,
                        upload_to="",
                        verbose_name="car_insurance",
                    ),
                ),
                (
                    "car_images",
                    models.CharField(
                        max_length=25500, null=True, verbose_name="car_images"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="status"
                    ),
                ),
            ],
            options={
                "verbose_name": "Car Registration",
                "verbose_name_plural": "Car Registration",
            },
        ),
        migrations.CreateModel(
            name="Client_login",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "datetime",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "user_ip",
                    models.CharField(max_length=255, null=True, verbose_name="user_ip"),
                ),
                (
                    "email",
                    models.EmailField(max_length=255, null=True, verbose_name="email"),
                ),
                (
                    "password",
                    models.CharField(
                        max_length=255, null=True, verbose_name="password"
                    ),
                ),
                (
                    "user_type",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="user_type"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="status"
                    ),
                ),
            ],
            options={
                "verbose_name": "Clients Login",
                "verbose_name_plural": "Clients Login",
            },
        ),
        migrations.CreateModel(
            name="client_token_authentication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        unique=True,
                        verbose_name="Email",
                    ),
                ),
                (
                    "is_email_verified",
                    models.BooleanField(
                        default=False, null=True, verbose_name="Email verification"
                    ),
                ),
                (
                    "user_phonenumber",
                    models.CharField(
                        default=None,
                        max_length=12,
                        null=True,
                        unique=True,
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "last_otp",
                    models.IntegerField(
                        default=None, null=True, verbose_name="Last OTP"
                    ),
                ),
                (
                    "last_otp_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Last OTP time"
                    ),
                ),
                (
                    "accessToken",
                    models.TextField(
                        blank=True, default=None, null=True, verbose_name="Access Token"
                    ),
                ),
                (
                    "refreshToken",
                    models.TextField(
                        blank=True,
                        default=None,
                        null=True,
                        verbose_name="Refresh Token",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Driver_Reg",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "datetime",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "driver_id",
                    models.CharField(
                        max_length=255, null=True, verbose_name="driver_id"
                    ),
                ),
                (
                    "driver_name",
                    models.CharField(
                        max_length=255, null=True, verbose_name="driver_name"
                    ),
                ),
                (
                    "driver_address",
                    models.CharField(
                        max_length=255, null=True, verbose_name="driver_address"
                    ),
                ),
                (
                    "driver_mobile",
                    models.CharField(
                        max_length=255, null=True, verbose_name="driver_mobile"
                    ),
                ),
                (
                    "driver_email",
                    models.CharField(
                        max_length=255, null=True, verbose_name="driver_email"
                    ),
                ),
                (
                    "languages",
                    models.CharField(
                        max_length=255, null=True, verbose_name="languages"
                    ),
                ),
                (
                    "working_hours",
                    models.CharField(
                        max_length=255, null=True, verbose_name="working_hours"
                    ),
                ),
                (
                    "licence_no",
                    models.CharField(
                        max_length=255, null=True, verbose_name="licence_no"
                    ),
                ),
                (
                    "adhar_card",
                    models.FileField(
                        default="0",
                        max_length=255,
                        null=True,
                        upload_to="",
                        verbose_name="addhar_card",
                    ),
                ),
                (
                    "licence_doc",
                    models.FileField(
                        default="0",
                        max_length=255,
                        null=True,
                        upload_to="",
                        verbose_name="licence_doc",
                    ),
                ),
                (
                    "picture",
                    models.FileField(
                        default="0",
                        max_length=255,
                        null=True,
                        upload_to="",
                        verbose_name="picture",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="status"
                    ),
                ),
            ],
            options={
                "verbose_name": "Car Driver Registration",
                "verbose_name_plural": "Car Driver Registration",
            },
        ),
        migrations.CreateModel(
            name="Reg_Hotel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "datetime",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "hotel_code",
                    models.CharField(
                        max_length=255, null=True, verbose_name="hotel_id"
                    ),
                ),
                (
                    "hotel_name",
                    models.CharField(
                        max_length=255, null=True, verbose_name="hotel_name"
                    ),
                ),
                (
                    "hotel_address",
                    models.TextField(
                        max_length=1000, null=True, verbose_name="hotel_address"
                    ),
                ),
                (
                    "hotel_city",
                    models.CharField(
                        max_length=255, null=True, verbose_name="hotel_city"
                    ),
                ),
                (
                    "hotel_state",
                    models.CharField(
                        max_length=255, null=True, verbose_name="hotel_state"
                    ),
                ),
                (
                    "geo_location",
                    models.CharField(
                        max_length=255, null=True, verbose_name="geo_location"
                    ),
                ),
                (
                    "pin_code",
                    models.CharField(max_length=255, null=True, verbose_name="pincode"),
                ),
                (
                    "room_rates",
                    models.CharField(max_length=255, null=True, verbose_name="rates"),
                ),
                (
                    "hotel_facilites",
                    models.TextField(
                        max_length=5000, null=True, verbose_name="facilites"
                    ),
                ),
                (
                    "max_guests_limit",
                    models.CharField(max_length=255, null=True, verbose_name="limits"),
                ),
                (
                    "hotel_images",
                    models.CharField(
                        max_length=25500, null=True, verbose_name="images"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="status"
                    ),
                ),
            ],
            options={
                "verbose_name": "Hotel Registration",
                "verbose_name_plural": "Hotel Registration",
            },
        ),
        migrations.CreateModel(
            name="Tour_locations",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "datetime",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "locations",
                    models.CharField(
                        max_length=255, null=True, verbose_name="locations"
                    ),
                ),
                (
                    "location_image",
                    models.CharField(
                        max_length=25500, null=True, verbose_name="location_image"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="status"
                    ),
                ),
            ],
            options={
                "verbose_name": "Tour Locations",
                "verbose_name_plural": "Tour Locations",
            },
        ),
        migrations.CreateModel(
            name="Tour_Packages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "datetime",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "location_ids",
                    models.CharField(
                        max_length=255, null=True, verbose_name="location_ids"
                    ),
                ),
                (
                    "package_amount",
                    models.CharField(
                        max_length=255, null=True, verbose_name="package_amount"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="status"
                    ),
                ),
            ],
            options={
                "verbose_name": "Tour Packages",
                "verbose_name_plural": "Tour Packages",
            },
        ),
        migrations.CreateModel(
            name="User_Register",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "datetime",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "user_id",
                    models.CharField(max_length=255, null=True, verbose_name="user_id"),
                ),
                (
                    "user_ip",
                    models.CharField(max_length=255, null=True, verbose_name="user_ip"),
                ),
                (
                    "name",
                    models.CharField(max_length=255, null=True, verbose_name="name"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, null=True, unique=True, verbose_name="email"
                    ),
                ),
                (
                    "mobile",
                    models.CharField(max_length=255, null=True, verbose_name="mobile"),
                ),
                (
                    "password",
                    models.CharField(
                        max_length=255, null=True, verbose_name="password"
                    ),
                ),
                (
                    "user_type",
                    models.CharField(
                        default="shangkai",
                        max_length=255,
                        null=True,
                        verbose_name="user_type",
                    ),
                ),
                (
                    "address",
                    models.TextField(
                        default="0", max_length=255, null=True, verbose_name="address"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="city"
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="state"
                    ),
                ),
                (
                    "pin_code",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="pin_code"
                    ),
                ),
                (
                    "voter_id",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="voter_id"
                    ),
                ),
                (
                    "whatsapp_no",
                    models.CharField(
                        default="0",
                        max_length=12,
                        null=True,
                        verbose_name="whatsapp_no",
                    ),
                ),
                (
                    "emergency_no",
                    models.CharField(
                        default="0",
                        max_length=12,
                        null=True,
                        verbose_name="emergency_no",
                    ),
                ),
                (
                    "bank_name",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="bank_name"
                    ),
                ),
                (
                    "bank_branch",
                    models.CharField(
                        default="0",
                        max_length=255,
                        null=True,
                        verbose_name="bank_branch",
                    ),
                ),
                (
                    "account_no",
                    models.CharField(
                        default="0",
                        max_length=255,
                        null=True,
                        verbose_name="account_no",
                    ),
                ),
                (
                    "ifsc_code",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="ifsc_code"
                    ),
                ),
                (
                    "otp",
                    models.CharField(max_length=255, null=True, verbose_name="otp"),
                ),
                (
                    "image",
                    models.FileField(
                        default="0",
                        max_length=255,
                        null=True,
                        upload_to="",
                        verbose_name="image",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="status"
                    ),
                ),
            ],
            options={
                "verbose_name": "Clients Registration",
                "verbose_name_plural": "Clients Registration",
            },
        ),
        migrations.CreateModel(
            name="TourGuide_Reg",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "datetime",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "guider_name",
                    models.CharField(
                        max_length=255, null=True, verbose_name="guider_name"
                    ),
                ),
                (
                    "about_guider",
                    models.TextField(
                        max_length=255, null=True, verbose_name="about_guider"
                    ),
                ),
                (
                    "guider_address",
                    models.TextField(
                        max_length=255, null=True, verbose_name="guider_address"
                    ),
                ),
                (
                    "guider_mobile",
                    models.CharField(
                        max_length=255, null=True, verbose_name="guider_mobile"
                    ),
                ),
                (
                    "guider_email",
                    models.CharField(
                        max_length=255, null=True, verbose_name="guider_email"
                    ),
                ),
                (
                    "languages",
                    models.CharField(
                        max_length=255, null=True, verbose_name="languages"
                    ),
                ),
                (
                    "adhar_card",
                    models.FileField(
                        default="0",
                        max_length=255,
                        null=True,
                        upload_to="",
                        verbose_name="addhar_card",
                    ),
                ),
                (
                    "licence_doc",
                    models.FileField(
                        default="0",
                        max_length=255,
                        null=True,
                        upload_to="",
                        verbose_name="licence_doc",
                    ),
                ),
                (
                    "picture",
                    models.FileField(
                        default="0",
                        max_length=255,
                        null=True,
                        upload_to="",
                        verbose_name="picture",
                    ),
                ),
                (
                    "rating",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="rating"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="status"
                    ),
                ),
                (
                    "packages",
                    models.ForeignKey(
                        db_constraint=False,
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clients.tour_packages",
                    ),
                ),
                (
                    "tour_locations",
                    models.ForeignKey(
                        db_constraint=False,
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clients.tour_locations",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        db_constraint=False,
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clients.user_register",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tour Guide Registration",
                "verbose_name_plural": "Tour Guide Registration",
            },
        ),
        migrations.AddField(
            model_name="tour_packages",
            name="user",
            field=models.ForeignKey(
                db_constraint=False,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="clients.user_register",
            ),
        ),
        migrations.AddField(
            model_name="tour_locations",
            name="user",
            field=models.ForeignKey(
                db_constraint=False,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="clients.user_register",
            ),
        ),
        migrations.CreateModel(
            name="Room_Register",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "datetime",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "room_id",
                    models.CharField(max_length=255, null=True, verbose_name="room_id"),
                ),
                (
                    "room_type",
                    models.CharField(
                        max_length=255, null=True, verbose_name="room_type"
                    ),
                ),
                (
                    "bed_type",
                    models.TextField(
                        max_length=1000, null=True, verbose_name="bed_type"
                    ),
                ),
                (
                    "totel_beds",
                    models.CharField(
                        max_length=255, null=True, verbose_name="totel_beds"
                    ),
                ),
                (
                    "room_rates",
                    models.CharField(max_length=255, null=True, verbose_name="rates"),
                ),
                (
                    "room_facilites",
                    models.TextField(
                        max_length=5000, null=True, verbose_name="facilites"
                    ),
                ),
                (
                    "max_guests_limit",
                    models.CharField(max_length=255, null=True, verbose_name="limits"),
                ),
                (
                    "no_rooms",
                    models.CharField(
                        max_length=255, null=True, verbose_name="no_of_rooms"
                    ),
                ),
                (
                    "checkin_date",
                    models.CharField(
                        max_length=255, null=True, verbose_name="checkin_date"
                    ),
                ),
                (
                    "checkout_date",
                    models.CharField(
                        max_length=255, null=True, verbose_name="checkout_date"
                    ),
                ),
                (
                    "rating",
                    models.CharField(max_length=255, null=True, verbose_name="rating"),
                ),
                (
                    "tags",
                    models.TextField(max_length=255, null=True, verbose_name="tags"),
                ),
                (
                    "extra_services",
                    models.TextField(
                        max_length=255, null=True, verbose_name="extra_services"
                    ),
                ),
                (
                    "room_images",
                    models.CharField(
                        max_length=25500, null=True, verbose_name="images"
                    ),
                ),
                (
                    "states",
                    models.CharField(
                        default="0", max_length=255, null=True, verbose_name="status"
                    ),
                ),
                (
                    "hotel_id",
                    models.ForeignKey(
                        db_constraint=False,
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clients.reg_hotel",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        db_constraint=False,
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clients.user_register",
                    ),
                ),
            ],
            options={
                "verbose_name": "Room Registration",
                "verbose_name_plural": "Room Registration",
            },
        ),
    ]
