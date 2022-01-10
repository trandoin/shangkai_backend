from django.contrib import admin
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
# from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.utils.timezone import utc
from .models import (
    Account_Details,
    Cabs_Reg,
    Driver_Reg,
    Reg_Hotel,
    Room_Register,
    User_Register,
    client_token_authentication,
    Tour_locations,
    Tour_Packages,
    TourGuide_Reg,
)

# Register your models here.


class UserRegister(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
        "user_ip",
        "name",
        "email",
        "mobile",
        "password",
        "user_type",
        "image",
    ]


admin.site.register(User_Register, UserRegister)


class ClientTokenAuthentication(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "user_email",
        "user_phonenumber",
        "last_otp",
        "accessToken",
        "refreshToken",
    ]


admin.site.register(client_token_authentication, ClientTokenAuthentication)


##  ========= HOTELS ==========##


class HotelRegister(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "hotel_cat",
        "hotel_code",
        "hotel_name",
        "hotel_address",
        "hotel_city",
        "hotel_state",
        "geo_location",
        "pin_code",
        "room_rates",
        "hotel_facilites",
        "max_guests_limit",
        "hotel_images",
        "status",
    ]


admin.site.register(Reg_Hotel, HotelRegister)


class RoomRegister(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "hotel_id",
        "room_id",
        "room_type",
        "bed_type",
        "totel_beds",
        "room_rates",
        "room_facilites",
        "max_guests_limit",
        "no_rooms",
        "rating",
        "tags",
        "extra_services",
        "room_images",
        "states",
    ]


admin.site.register(Room_Register, RoomRegister)


class DriverRegistration(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "driver_id",
        "driver_name",
        "driver_address",
        "driver_mobile",
        "driver_email",
        "languages",
        "working_hours",
        "licence_no",
        "adhar_card",
        "licence_doc",
        "picture",
    ]


admin.site.register(Driver_Reg, DriverRegistration)


class CarRegistration(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "driver",
        "car_code",
        "car_name",
        "car_type",
        "capacity",
        "vehicle_no",
        "car_mou",
        "pickup_point",
        "destination",
        "checkin_date",
        "checkout_date",
        "car_rating",
        "car_rc",
        "car_insurance",
        "car_images",
        "status",
    ]


admin.site.register(Cabs_Reg, CarRegistration)


class Tourlocations(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "locations",
        "location_image",
    ]


admin.site.register(Tour_locations, Tourlocations)


class TourPackages(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "location_ids",
        "package_amount",
    ]


admin.site.register(Tour_Packages, TourPackages)


class TourGuideReg(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "tour_locations",
        "packages",
        "guider_name",
        "about_guider",
        "guider_address",
        "guider_mobile",
        "guider_email",
        "languages",
        "adhar_card",
        "licence_doc",
        "picture",
        "rating",
    ]


admin.site.register(TourGuide_Reg, TourGuideReg)


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


admin.site.register(Account_Details, AccountDetails)

AdminSite.site_header = "Shangkai.in"
AdminSite.site_title = "Administrator Panel"
AdminSite.index_title = "Shangkai.in Administrator Panel"
