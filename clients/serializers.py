from rest_framework.serializers import ModelSerializer
from .models import (
    HotelImages,
    Reg_Hotel,
    Room_Register,
    RoomImages,
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
        fields = ["id","user_ip","name","email","mobile","password","user_type"]

        extra_kwargs = {
            "password": {"write_only": True},
        }        


class ClientloginSerializer(ModelSerializer):
    class Meta:
        model = Client_login
        fields = "__all__"


class clienttokenauthenticationSerializer(ModelSerializer):
    class Meta:
        model = client_token_authentication
        fields = "__all__"

class HotelImageSerializer(ModelSerializer):
    class Meta:
        model = HotelImages
        fields = "__all__"
        
class RoomImageSerializer(ModelSerializer):
    class Meta:
        model = RoomImages
        fields = "__all__"

class HotelRegisterSerializer(ModelSerializer):
    class Meta:
        model = Reg_Hotel
        fields = "__all__"


class RoomRegisterSerializer(ModelSerializer):
    class Meta:
        model = Room_Register
        fields = "__all__"

class HotelViewSerializer(ModelSerializer):
    gallery_images = HotelImageSerializer(many=True, read_only=True)
    class Meta:
        model = Reg_Hotel
        depth = 1
        fields = ["id","user","hotel_cat","hotel_code","hotel_name","hotel_address","hotel_city","hotel_state","geo_location","pin_code","room_rates","hotel_facilites","max_guests_limit","hotel_images","title_image","status","gallery_images"]
        read_only_fields = ["__all__"]
        
class RoomViewSerializer(ModelSerializer):
    gallery_images = RoomImageSerializer(many=True, read_only=True)
    class Meta:
        model = Room_Register
        depth = 1
        fields = ["id","about","user","hotel_id","room_id","room_type","bed_type","totel_beds","room_rates","room_facilites","max_guests_limit","no_rooms","checkin_date","checkout_date","rating","tags","extra_services","status","room_images","title_image","gallery_images"]
        read_only_fields = ["__all__"]

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
        
class TourPackagesViewSerializer(ModelSerializer):
    class Meta:
        model = Tour_Packages
        depth = 1
        fields = "__all__"


class TourGuideRegSerializer(ModelSerializer):
    class Meta:
        model = TourGuide_Reg
        fields = "__all__"
        
class TourGuideRegViewSerializer(ModelSerializer):
    class Meta:
        model = TourGuide_Reg
        depth = 2
        fields = "__all__"
