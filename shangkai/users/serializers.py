from rest_framework.serializers import ModelSerializer
from .models import (
    # Hotel_Booking,
    Normal_UserReg,
)


class NormalUserRegisterSerializer(ModelSerializer):
    class Meta:
        model = Normal_UserReg
        fields = "__all__"


# class HotelBookingSerializer(ModelSerializer):
#     class Meta:
#         model = Hotel_Booking
#         fields = "__all__"
