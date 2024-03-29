from rest_framework.serializers import ModelSerializer
from .models import (
    About_Us,
    Footer_Copyright,
    HotSpot_Images,
    Hotspot_Category,
    Hot_Spots,
    Comments_All,
    Payment_Transaction,
    Hotel_Category,
    My_Trips,
    My_Trips_Days,
    Admin_Notification,
    Contact_Us,
    Blog_Category,
    Blog_Post,
    BlogPost_Comments,
    Tracking,
)

class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = About_Us
        fields = "__all__"


class FooterSerializer(ModelSerializer):
    class Meta:
        model = Footer_Copyright
        fields = "__all__"


class ContactUsSerializer(ModelSerializer):
    class Meta:
        model = Contact_Us
        fields = "__all__"


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Admin_Notification
        fields = "__all__"


class BlogCategorySerializer(ModelSerializer):
    class Meta:
        model = Blog_Category
        fields = "__all__"


class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = Blog_Post
        fields = "__all__"


class BlogPostCommentsSerializer(ModelSerializer):
    class Meta:
        model = BlogPost_Comments
        fields = "__all__"


class HotspotCategorySerializer(ModelSerializer):
    class Meta:
        model = Hotspot_Category
        fields = "__all__"


class HotelCategorySerializer(ModelSerializer):
    class Meta:
        model = Hotel_Category
        fields = "__all__"

class HotSpotImageSerializer(ModelSerializer):
    class Meta:
        model = HotSpot_Images
        fields = "__all__"

class HotSpotsSerializer(ModelSerializer):
    gallery_images = HotSpotImageSerializer(many=True,read_only=True)
    class Meta:
        model = Hot_Spots
        fields = ("__all__","gallery_images")

class TrackingSerializer(ModelSerializer):
    class Meta:
        model = Tracking
        fields = "__all__"

class MyTripsSerializer(ModelSerializer):
    class Meta:
        model = My_Trips
        fields = "__all__"


class MyTripsDaysSerializer(ModelSerializer):
    class Meta:
        model = My_Trips_Days
        fields = "__all__"


class CommentsAllSerializer(ModelSerializer):
    class Meta:
        model = Comments_All
        fields = "__all__"


class PaymentTransactionAllSerializer(ModelSerializer):
    class Meta:
        model = Payment_Transaction
        fields = "__all__"
