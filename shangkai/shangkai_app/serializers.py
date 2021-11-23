from rest_framework.serializers import ModelSerializer
from .models import (
   About_Us,
   Footer_Copyright,
   Hotspot_Category,
   Hot_Spots,
#    Comments_All,
   Payment_Transaction,
#    Hotel_Category,
   
)


class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = About_Us
        fields = "__all__"

class FooterSerializer(ModelSerializer):
    class Meta:
        model = Footer_Copyright
        fields = "__all__"  

class HotspotCategorySerializer(ModelSerializer):
    class Meta:
        model = Hotspot_Category
        fields = "__all__"  

# class HotelCategorySerializer(ModelSerializer):
#     class Meta:
#         model = Hotel_Category
#         fields = "__all__"  

class HotSpotsSerializer(ModelSerializer):
    class Meta:
        model = Hot_Spots
        fields = "__all__"  

# class CommentsAllSerializer(ModelSerializer):
#     class Meta:
#         model = Comments_All
#         fields = "__all__" 

class PaymentTransactionAllSerializer(ModelSerializer):
    class Meta:
        model = Payment_Transaction
        fields = "__all__"                                        