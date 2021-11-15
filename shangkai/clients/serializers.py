from rest_framework.serializers import ModelSerializer
from .models import (
    Reg_Hotel,
    Room_Register,
    User_Register,
)


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User_Register
        fields = "__all__"


class HotelRegisterSerializer(ModelSerializer):
    class Meta:
        model = Reg_Hotel
        fields = "__all__"


class RoomRegisterSerializer(ModelSerializer):
    class Meta:
        model = Room_Register
        fields = "__all__"
