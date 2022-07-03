from rest_framework.serializers import ModelSerializer
from .models import (
    Reg_Hotel,
    Room_Register,
    User_Register,
    Driver_Reg,
    Cabs_Reg,
    Client_login,
    client_token_authentication,
    Tour_locations,
    Tour_Packages,
    TourGuide_Reg,
)


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User_Register
        fields = "__all__"


class ClientloginSerializer(ModelSerializer):
    class Meta:
        model = Client_login
        fields = "__all__"


class clienttokenauthenticationSerializer(ModelSerializer):
    class Meta:
        model = client_token_authentication
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


class TourlocationsSerializer(ModelSerializer):
    class Meta:
        model = Tour_locations
        fields = "__all__"


class TourPackagesSerializer(ModelSerializer):
    class Meta:
        model = Tour_Packages
        fields = "__all__"


class TourGuideRegSerializer(ModelSerializer):
    class Meta:
        model = TourGuide_Reg
        fields = "__all__"
