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

from clients.models import (
    Cabs_Reg,
    Reg_Hotel,
    Room_Register,
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

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        user_ip = request.POST.get("user_ip", None)
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        mobile = request.POST.get("mobile", None)
        password = request.POST.get("password", None)
        image = request.POST.get("image", None)

        users_inst = Normal_UserReg.objects.create(
            user_id=user_inst,
            user_ip=user_ip,
            name=name,
            email=email,
            mobile=mobile,
            password=password,
            image=image,
        )
        users_inst.save()

        users_data = serializers.NormalUserRegisterSerializer(
            Normal_UserReg.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)    

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

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        user_ip = request.POST.get("user_ip", None)
        hotel_id = request.POST.get("hotel_id", None)
        room_id = request.POST.get("room_id", None)
        hotel_bookid = request.POST.get("hotel_bookid", None)
        check_in_date = request.POST.get("check_in_date", None)
        check_in_time = request.POST.get("check_in_time", None)
        check_out_date = request.POST.get("check_out_date", None)
        check_out_time = request.POST.get("check_out_time", None)
        guest_no = request.POST.get("guest_no", None)
        rooms = request.POST.get("rooms", None)
        amount_booking = request.POST.get("amount_booking", None)

        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            hotel_inst = Reg_Hotel.objects.get(id=hotel_id)
            room_inst = Room_Register.objects.get(id=room_id)
        except:

            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = User_Cab_Booking.objects.create(
            user_id=user_inst,
            user_ip=user_ip,
            hotel_id=hotel_inst,
            room_id=room_inst,
            hotel_bookid=hotel_bookid,
            check_in_date=check_in_date,
            check_in_time=check_in_time,
            check_out_date=check_out_date,
            check_out_time=check_out_time,
            guest_no=guest_no,
            rooms=rooms,
            amount_booking=amount_booking,
        )
        users_inst.save()

        users_data = serializers.CabBookingSerializer(
            User_Cab_Booking.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)      


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

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        user_ip = request.POST.get("user_ip", None)
        car_id = request.POST.get("car_id", None)
        driver_id = request.POST.get("driver_id", None)
        cab_bookid = request.POST.get("cab_bookid", None)
        check_in_date = request.POST.get("check_in_date", None)
        check_in_time = request.POST.get("check_in_time", None)
        check_out_date = request.POST.get("check_out_date", None)
        check_out_time = request.POST.get("check_out_time", None)
        start_from = request.POST.get("start_from", None)
        end_trip = request.POST.get("end_trip", None)
        distance = request.POST.get("distance", None)
        amount_booking = request.POST.get("amount_booking", None)
        no_guests = request.POST.get("no_guests", None)

        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            car_inst = Cabs_Reg.objects.get(id=car_id)
        except:

            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = User_Cab_Booking.objects.create(
            user_id=user_inst,
            user_ip=user_ip,
            car_id=car_inst,
            driver_id=driver_id,
            cab_bookid=cab_bookid,
            check_in_date=check_in_date,
            check_in_time=check_in_time,
            check_out_date=check_out_date,
            check_out_time=check_out_time,
            start_from=start_from,
            end_trip=end_trip,
            distance=distance,
            amount_booking=amount_booking,
            no_guests=no_guests,
        )
        users_inst.save()

        users_data = serializers.CabBookingSerializer(
            User_Cab_Booking.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)       

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