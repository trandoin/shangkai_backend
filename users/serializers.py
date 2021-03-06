from rest_framework.serializers import ModelSerializer

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

########### """"""""" ACCOUNTS DETAILS """""""""""" #############


class NormalUserRegisterSerializer(ModelSerializer):
    class Meta:
        model = Normal_UserReg
        fields = "__all__"


class AccountDetailsBookingSerializer(ModelSerializer):
    class Meta:
        model = User_Account_Details
        fields = "__all__"


class UserRatingsSerializer(ModelSerializer):
    class Meta:
        model = User_Ratings
        fields = "__all__"


########### """"""""" HOTELS """""""""""" #############


class HotelCartSerializer(ModelSerializer):
    class Meta:
        model = User_Hotel_Cart
        fields = "__all__"


class HotelBookingSerializer(ModelSerializer):
    class Meta:
        model = User_Hotel_Booking
        fields = "__all__"


class UserHotelPaymentSerializer(ModelSerializer):
    class Meta:
        model = User_Hotel_Payment
        fields = "__all__"


########### """"""""" CABS """""""""""" #############


class CabCartSerializer(ModelSerializer):
    class Meta:
        model = User_Cab_Cart
        fields = "__all__"


class CabBookingSerializer(ModelSerializer):
    class Meta:
        model = User_Cab_Booking
        fields = "__all__"


class UserCabPaymentSerializer(ModelSerializer):
    class Meta:
        model = User_Cab_Payment
        fields = "__all__"


########### """"""""" TRIPS """""""""""" #############


class UserTripCartSerializer(ModelSerializer):
    class Meta:
        model = User_Trip_Cart
        fields = "__all__"


class UserTripBookingSerializer(ModelSerializer):
    class Meta:
        model = User_Trip_Booking
        fields = "__all__"


class UserTripsPaymentSerializer(ModelSerializer):
    class Meta:
        model = User_Trips_Payment
        fields = "__all__"


#############"""""" TOUR GUIDE """"""""########


class UserGuideBookingSerializer(ModelSerializer):
    class Meta:
        model = User_Guide_Booking
        fields = "__all__"


#########""""""HOTSPOTS """"""#####


class UserHotspotsCartSerializer(ModelSerializer):
    class Meta:
        model = User_Hotspots_Cart
        fields = "__all__"


class UserHotspotsBookingsSerializer(ModelSerializer):
    class Meta:
        model = User_Hotspots_Bookings
        fields = "__all__"
