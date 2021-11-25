from rest_framework.serializers import ModelSerializer
from .models import (
    Reg_Hotel,
    Room_Register,
    User_Register,
    Driver_Reg,
    Cabs_Reg,
    Client_login,
)


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User_Register
        fields = "__all__"

class ClientloginSerializer(ModelSerializer):
    class Meta:
        model = Client_login
        fields = "__all__"


class HotelRegisterSerializer(ModelSerializer):
    class Meta:
        model = Reg_Hotel
        fields = "__all__"


class RoomRegisterSerializer(ModelSerializer):
    class Meta:
        model = Room_Register
        fields = "__all__"

class DriverRegisterSerializer(ModelSerializer):
    class Meta:
        model = Driver_Reg
        fields = "__all__"

class CabRegisterSerializer(ModelSerializer):
    class Meta:
        model = Cabs_Reg
        fields = "__all__"        
