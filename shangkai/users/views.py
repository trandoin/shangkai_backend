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

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        acc_holder = request.POST.get("acc_holder", None)
        account_no = request.POST.get("account_no", None)
        bannk_name = request.POST.get("bannk_name", None)
        bank_branch = request.POST.get("bank_branch", None)
        ifsc_code = request.POST.get("ifsc_code", None)
        bank_state = request.POST.get("bank_state", None)
        pan_card = request.POST.get("pan_card", None)

        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
        except:

            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = User_Account_Details.objects.create(
            user_id=user_id,
            acc_holder=acc_holder,
            account_no=account_no,
            bannk_name=bannk_name,
            bank_branch=bank_branch,
            ifsc_code=ifsc_code,
            bank_state=bank_state,
            pan_card=pan_card,
        )
        users_inst.save()

        users_data = serializers.AccountDetailsBookingSerializer(
            User_Account_Details.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)                            