from django.shortcuts import render
from rest_framework import serializers, viewsets
from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers

"""Model Package """
from .models import (
    User_Account_Details,
    User_Cab_Booking,
    User_Hotel_Booking,
    Normal_UserReg,
)


class UserRegisterViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_users = Normal_UserReg.objects.all()
            users_data_dic = serializers.NormalUserRegisterSerializer(
                sm_users, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)

class HotelBookingViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_hotel = User_Hotel_Booking.objects.all()
            hotel_data_dic = serializers.HotelBookingSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(hotel_data_dic.data, status=status.HTTP_200_OK)  


class CabBookingViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_hotel = User_Cab_Booking.objects.all()
            hotel_data_dic = serializers.CabBookingSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(hotel_data_dic.data, status=status.HTTP_200_OK)  

class AccounDetailsBookingViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_hotel = User_Account_Details.objects.all()
            hotel_data_dic = serializers.AccountDetailsBookingSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(hotel_data_dic.data, status=status.HTTP_200_OK)                        