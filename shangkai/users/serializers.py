from rest_framework.serializers import ModelSerializer
from .models import (
    Hotel_Booking,
    Normal_UserReg,
    # User_Booking,
)


class NormalUserRegisterSerializer(ModelSerializer):
    class Meta:
        model = Normal_UserReg
        fields = "__all__"


class HotelBookingSerializer(ModelSerializer):
    class Meta:
        model = Hotel_Booking
        fields = "__all__"
