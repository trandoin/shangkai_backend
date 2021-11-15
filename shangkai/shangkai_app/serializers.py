from rest_framework.serializers import ModelSerializer
from .models import (
   About_Us,
   Footer_Copyright,
)


class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = About_Us
        fields = "__all__"

class FooterSerializer(ModelSerializer):
    class Meta:
        model = Footer_Copyright
        fields = "__all__"        