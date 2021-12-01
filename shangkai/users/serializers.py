from rest_framework.serializers import ModelSerializer
from .models import (
    User_Account_Details,
    User_Cab_Booking,
    User_Hotel_Booking,
    Normal_UserReg,
    User_Hotel_Cart,
    User_Cab_Cart,
)


class NormalUserRegisterSerializer(ModelSerializer):
    class Meta:
        model = Normal_UserReg
        fields = "__all__"


class HotelBookingSerializer(ModelSerializer):
    class Meta:
        model = User_Hotel_Booking
        fields = "__all__"

class HotelCartSerializer(ModelSerializer):
    class Meta:
        model = User_Hotel_Cart
        fields = "__all__"        

class CabBookingSerializer(ModelSerializer):
    class Meta:
        model = User_Cab_Booking
        fields = "__all__"

class CabCartSerializer(ModelSerializer):
    class Meta:
        model = User_Cab_Cart
        fields = "__all__"


class AccountDetailsBookingSerializer(ModelSerializer):
    class Meta:
        model = User_Account_Details
        fields = "__all__"
