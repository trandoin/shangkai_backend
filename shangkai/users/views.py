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
    User_Guide_Booking,
    User_Hotel_Booking,
    Normal_UserReg,
    User_Hotel_Cart,
    User_Cab_Cart,
    User_Hotel_Payment,
    User_Trip_Cart,
    User_Cab_Payment,
    User_Trip_Booking,
    User_Trips_Payment,
)

from clients.models import (
    Cabs_Reg,
    Reg_Hotel,
    Room_Register,
    Driver_Reg,
    TourGuide_Reg,
    User_Register,
)
from shangkai_app.models import (
    My_Trips,
)


########### """"""""" ACCOUNTS DETAILS """""""""""" #############


class UserRegisterViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_users = Normal_UserReg.objects.filter(id=user_id)
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
            user_id=user_id,
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

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        name = request.POST.get("name", None)
        mobile = request.POST.get("mobile", None)
        password = request.POST.get("password", None)
        image = request.POST.get("image", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = Normal_UserReg.objects.get(id=pk)
            post_inst.name = name
            post_inst.mobile = mobile
            post_inst.password = password
            post_inst.image = image
            post_inst.is_edited = True
            post_inst.save()

            users_data = serializers.NormalUserRegisterSerializer(
                Normal_UserReg.objects.filter(id=post_inst.id), many=True
            )
            return Response(
                users_data.data,
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserLoginViewSet(viewsets.ViewSet):
    def create(self, request):

        email = request.POST.get("email", None)
        password = request.POST.get("password", None)

        if email is None and password is None:

            return Response(
                {"message": "Enter username & password !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            users_inst = Normal_UserReg.objects.filter(email=email, password=password)
            users_data_dic = serializers.NormalUserRegisterSerializer(
                users_inst, many=True
            )
        except:
            return Response(
                {"message": "Invalid username & password !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)


class AccounDetailsBookingViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_hotel = User_Account_Details.objects.all()
            account_data_dic = serializers.AccountDetailsBookingSerializer(
                sm_hotel, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for i in range(0, len(account_data_dic.data)):
            created_user_id = account_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                account_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                            "user_email": user_inst.email,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )

        return Response(account_data_dic.data, status=status.HTTP_200_OK)

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


########### """"""""" HOTELS """""""""""" #############


class HotelCartViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_hotel = User_Hotel_Cart.objects.filter(user=user_id)
            hotel_data_dic = serializers.HotelCartSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(hotel_data_dic.data)):
            created_user_id = hotel_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                hotel_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_hotel_id = hotel_data_dic.data[i].get("hotel_id")
            try:
                hotel_inst = Reg_Hotel.objects.get(id=created_hotel_id)

                hotel_data_dic.data[i].update(
                    {
                        "hotel_id": {
                            "id": hotel_inst.id,
                            "hotel_code": hotel_inst.hotel_code,
                            "hotel_name": hotel_inst.hotel_name,
                            "geo_location": hotel_inst.geo_location,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {
                        "hotel_id": {
                            "id": created_hotel_id,
                            "message": "Deleted Hotel",
                        }
                    }
                )
            created_room_id = hotel_data_dic.data[i].get("room_id")
            try:
                room_inst = Room_Register.objects.get(id=created_room_id)

                hotel_data_dic.data[i].update(
                    {
                        "room_id": {
                            "id": room_inst.id,
                            "room_id": room_inst.room_id,
                            "room_type": room_inst.room_type,
                            "bed_type": room_inst.bed_type,
                            # "room_images": room_inst.room_images,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {
                        "room_id": {
                            "id": created_room_id,
                            "message": "Deleted room",
                        }
                    }
                )

        return Response(hotel_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        hotel_id = request.POST.get("hotel_id", None)
        room_id = request.POST.get("room_id", None)
        check_in_date = request.POST.get("check_in_date", None)
        check_out_date = request.POST.get("check_out_date", None)
        guest_no = request.POST.get("guest_no", None)
        rooms = request.POST.get("rooms", None)
        amount_booking = request.POST.get("amount_booking", None)
        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            hotel_inst = Reg_Hotel.objects.get(id=hotel_id)
            room_inst = Room_Register.objects.get(id=room_id)
        except:

            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        hotel_cart_inst = User_Hotel_Cart.objects.create(
            user=user_inst,
            hotel_id=hotel_inst,
            room_id=room_inst,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            guest_no=guest_no,
            rooms=rooms,
            amount_booking=amount_booking,
        )
        hotel_cart_inst.save()

        hotel_cart_data = serializers.HotelCartSerializer(
            User_Hotel_Cart.objects.filter(id=hotel_cart_inst.id), many=True
        )
        return Response(hotel_cart_data.data[0], status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)
        cart_id = request.GET.get("cart_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_post_inst = User_Hotel_Cart.objects.filter(id=pk)
            scm_post_inst.delete()
            return Response(
                {"message": "Successfully Cart Removed"}, status=status.HTTP_200_OK
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)


class HotelBookingViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_hotel = User_Hotel_Booking.objects.filter(user=user_id)
            hotel_data_dic = serializers.HotelBookingSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(hotel_data_dic.data)):
            created_user_id = hotel_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                hotel_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_hotel_id = hotel_data_dic.data[i].get("hotel_id")
            try:
                hotel_inst = Reg_Hotel.objects.get(id=created_hotel_id)

                hotel_data_dic.data[i].update(
                    {
                        "hotel_id": {
                            "id": hotel_inst.id,
                            "hotel_code": hotel_inst.hotel_code,
                            "hotel_name": hotel_inst.hotel_name,
                            "geo_location": hotel_inst.geo_location,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {
                        "hotel_id": {
                            "id": created_hotel_id,
                            "message": "Deleted Hotel",
                        }
                    }
                )
            created_room_id = hotel_data_dic.data[i].get("room_id")
            try:
                room_inst = Room_Register.objects.get(id=created_room_id)

                hotel_data_dic.data[i].update(
                    {
                        "room_id": {
                            "id": room_inst.id,
                            "room_id": room_inst.room_id,
                            "room_type": room_inst.room_type,
                            "bed_type": room_inst.bed_type,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {
                        "room_id": {
                            "id": created_room_id,
                            "message": "Deleted room",
                        }
                    }
                )

        return Response(hotel_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        user_ip = request.POST.get("client_id", None)
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

        users_inst = User_Hotel_Booking.objects.create(
            user=user_inst,
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

        users_data = serializers.HotelBookingSerializer(
            User_Hotel_Booking.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)
        book_id = request.GET.get("book_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_post_inst = User_Hotel_Booking.objects.filter(id=pk)
            scm_post_inst.delete()
            return Response(
                {"message": "Hotel Booking Removed Successfully"},
                status=status.HTTP_200_OK,
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)


class HotelPaymentViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_hotel = User_Hotel_Payment.objects.filter(user=user_id)
            hotel_data_dic = serializers.UserHotelPaymentSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(hotel_data_dic.data)):
            created_user_id = hotel_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                hotel_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_hotel_id = hotel_data_dic.data[i].get("hotel_booking")
            try:
                hotel_inst = User_Hotel_Booking.objects.get(id=created_hotel_id)

                hotel_data_dic.data[i].update(
                    {
                        "hotel_booking": {
                            "id": hotel_inst.id,
                            # "hotel_id": hotel_inst.hotel_id,
                            # "room_id":hotel_inst.room_id,
                            "hotel_bookid": hotel_inst.hotel_bookid,
                            "check_in_date": hotel_inst.check_in_date,
                            "check_in_time": hotel_inst.check_in_time,
                            "check_out_date": hotel_inst.check_out_date,
                            "check_out_time": hotel_inst.check_out_time,
                            "guest_no": hotel_inst.guest_no,
                            "rooms": hotel_inst.rooms,
                            "amount_booking": hotel_inst.amount_booking,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {
                        "hotel_booking": {
                            "id": created_hotel_id,
                            "message": "Deleted Hotel Booking",
                        }
                    }
                )

        return Response(hotel_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        hotel_booking_id = request.POST.get("hotel_booking_id", None)
        payment_id = request.POST.get("payment_id", None)
        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            hotel_booking_inst = User_Hotel_Booking.objects.get(id=hotel_booking_id)
        except:

            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = User_Hotel_Payment.objects.create(
            user=user_inst,
            hotel_booking=hotel_booking_inst,
            payment_id=payment_id,
        )
        users_inst.save()

        users_data = serializers.UserHotelPaymentSerializer(
            User_Hotel_Payment.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)


########### """"""""" CABS """""""""""" #############


class CabCartViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_hotel = User_Cab_Cart.objects.filter(user=user_id)
            cabs_data_dic = serializers.CabCartSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(cabs_data_dic.data)):
            created_user_id = cabs_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                cabs_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_cab_id = cabs_data_dic.data[i].get("car_id")
            try:
                cab_inst = Cabs_Reg.objects.get(id=created_cab_id)

                cabs_data_dic.data[i].update(
                    {
                        "car_id": {
                            "id": cab_inst.id,
                            "car_code": cab_inst.car_code,
                            "car_name": cab_inst.car_name,
                            "vehicle_no": cab_inst.vehicle_no,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {
                        "car_id": {
                            "id": created_cab_id,
                            "message": "Deleted cab",
                        }
                    }
                )
            created_driver_id = cabs_data_dic.data[i].get("driver_id")
            try:
                driver_inst = Driver_Reg.objects.get(id=created_driver_id)

                cabs_data_dic.data[i].update(
                    {
                        "driver_id": {
                            "id": driver_inst.id,
                            "driver_name": driver_inst.driver_name,
                            "driver_mobile": driver_inst.driver_mobile,
                            "driver_email": driver_inst.driver_email,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {
                        "driver_id": {
                            "id": created_driver_id,
                            "message": "Deleted Driver",
                        }
                    }
                )
        return Response(cabs_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        car_id = request.POST.get("car_id", None)
        driver_id = request.POST.get("driver_id", None)
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
            driver_inst = Driver_Reg.objects.get(id=driver_id)
        except:

            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = User_Cab_Cart.objects.create(
            user=user_inst,
            car_id=car_inst,
            driver_id=driver_inst,
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

        users_data = serializers.CabCartSerializer(
            User_Cab_Cart.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)
        cart_id = request.GET.get("cart_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_post_inst = User_Cab_Cart.objects.filter(id=pk)
            scm_post_inst.delete()
            return Response(
                {"message": "Successfully Cart Removed"}, status=status.HTTP_200_OK
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)


class CabBookingViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_hotel = User_Cab_Booking.objects.filter(user=user_id)
            cabs_data_dic = serializers.CabBookingSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(cabs_data_dic.data)):
            created_user_id = cabs_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                cabs_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_cab_id = cabs_data_dic.data[i].get("car_id")
            try:
                cab_inst = Cabs_Reg.objects.get(id=created_cab_id)

                cabs_data_dic.data[i].update(
                    {
                        "car_id": {
                            "id": cab_inst.id,
                            "car_code": cab_inst.car_code,
                            "car_name": cab_inst.car_name,
                            "vehicle_no": cab_inst.vehicle_no,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {
                        "car_id": {
                            "id": created_cab_id,
                            "message": "Deleted cab",
                        }
                    }
                )
            created_driver_id = cabs_data_dic.data[i].get("driver_id")
            try:
                driver_inst = Driver_Reg.objects.get(id=created_driver_id)

                cabs_data_dic.data[i].update(
                    {
                        "driver_id": {
                            "id": driver_inst.id,
                            "driver_name": driver_inst.driver_name,
                            "driver_mobile": driver_inst.driver_mobile,
                            "driver_email": driver_inst.driver_email,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {
                        "driver_id": {
                            "id": created_driver_id,
                            "message": "Deleted Driver",
                        }
                    }
                )
        return Response(cabs_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        user_ip = request.POST.get("client_id", None)
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
            driver_inst = Driver_Reg.objects.get(id=driver_id)
        except:

            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = User_Cab_Booking.objects.create(
            user=user_inst,
            user_ip=user_ip,
            car_id=car_inst,
            driver_id=driver_inst,
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

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)
        book_id = request.GET.get("book_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_post_inst = User_Cab_Booking.objects.filter(id=pk)
            scm_post_inst.delete()
            return Response(
                {"message": "Cab Booking Removed Successfully"},
                status=status.HTTP_200_OK,
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)


class CabPaymentViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_cab_booking = User_Cab_Payment.objects.filter(user=user_id)
            cab_booking_data_dic = serializers.UserCabPaymentSerializer(
                sm_cab_booking, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(cab_booking_data_dic.data)):
            created_user_id = cab_booking_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                cab_booking_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                cab_booking_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_cab_booking_id = cab_booking_data_dic.data[i].get("cab_booking")
            try:
                cab_booking_inst = User_Cab_Booking.objects.get(
                    id=created_cab_booking_id
                )

                cab_booking_data_dic.data[i].update(
                    {
                        "cab_booking": {
                            "id": cab_booking_inst.id,
                            "cab_bookid": cab_booking_inst.cab_bookid,
                            # "car_id":cab_booking_inst.car_id,
                            # "driver_id":cab_booking_inst.driver_id,
                            "check_in_date": cab_booking_inst.check_in_date,
                            "check_in_time": cab_booking_inst.check_in_time,
                            "check_out_date": cab_booking_inst.check_out_date,
                            "check_out_time": cab_booking_inst.check_out_time,
                            "end_trip": cab_booking_inst.end_trip,
                            "amount_booking": cab_booking_inst.amount_booking,
                            "no_guests": cab_booking_inst.no_guests,
                        }
                    }
                )
            except:
                cab_booking_data_dic.data[i].update(
                    {
                        "cab_booking": {
                            "id": created_cab_booking_id,
                            "message": "Deleted Cab Booking",
                        }
                    }
                )

        return Response(cab_booking_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        cab_booking = request.POST.get("cab_booking", None)
        payment_id = request.POST.get("payment_id", None)
        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            cab_booking_inst = User_Cab_Booking.objects.get(id=cab_booking)
        except:

            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = User_Cab_Payment.objects.create(
            user=user_inst,
            cab_booking=cab_booking_inst,
            payment_id=payment_id,
        )
        users_inst.save()

        users_data = serializers.UserCabPaymentSerializer(
            User_Cab_Payment.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)


########### """"""""" TRIPS """""""""""" #############


class UserTripsCartViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_hotel = User_Trip_Cart.objects.filter(user=user_id)
            account_data_dic = serializers.UserTripCartSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for i in range(0, len(account_data_dic.data)):
            created_user_id = account_data_dic.data[i].get("trip_id")
            try:
                user_inst = My_Trips.objects.get(id=created_user_id)

                account_data_dic.data[i].update(
                    {
                        "trip_id": {
                            "id": user_inst.id,
                            "trip_title": user_inst.title,
                            "trip_category": user_inst.category,
                            "trip_price": user_inst.price,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {"trip_id": {"id": created_user_id, "message": "Deleted Trip"}}
                )

        return Response(account_data_dic.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)
        cart_id = request.GET.get("cart_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_post_inst = User_Trip_Cart.objects.filter(id=pk)
            scm_post_inst.delete()
            return Response(
                {"message": "Successfully Cart Removed"}, status=status.HTTP_200_OK
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        cart_id = request.POST.get("cart_id", None)
        trip_cart_status = request.POST.get("cart_status", None)

        if pk is None and user_id is None:
            return Response(
                {"message": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = User_Trip_Cart.objects.get(id=pk)
            post_inst.trip_cart_status = trip_cart_status
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Cart Updated Sucessfully"},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Sorry No data found with this cart id"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        trip_id = request.POST.get("trip_id", None)
        no_guests = request.POST.get("no_guests", None)

        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            trip_inst = My_Trips.objects.get(id=trip_id)
        except:

            return Response(
                {"message": "Invalid Request!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = User_Trip_Cart.objects.create(
            user_id=user_id,
            trip_id=trip_inst,
            no_guests=no_guests,
        )
        users_inst.save()

        users_data = serializers.UserTripCartSerializer(
            User_Trip_Cart.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)


class UserTripsBookingViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_hotel = User_Trip_Booking.objects.filter(user=user_id)
            account_data_dic = serializers.UserTripBookingSerializer(
                sm_hotel, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for i in range(0, len(account_data_dic.data)):
            created_user_id = account_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                account_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_name": user_inst.name,
                            "user_mobile": user_inst.mobile,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted User"}}
                )
            created_user_id = account_data_dic.data[i].get("trip_id")
            try:
                user_inst = My_Trips.objects.get(id=created_user_id)

                account_data_dic.data[i].update(
                    {
                        "trip_id": {
                            "id": user_inst.id,
                            "trip_title": user_inst.title,
                            "trip_category": user_inst.category,
                            "trip_price": user_inst.price,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {"trip_id": {"id": created_user_id, "message": "Deleted Trip"}}
                )

        return Response(account_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        trip_id = request.POST.get("trip_id", None)
        trip_amount = request.POST.get("trip_amount", None)
        no_guests = request.POST.get("no_guests", None)

        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            trip_inst = My_Trips.objects.get(id=trip_id)
        except:

            return Response(
                {"message": "Invalid Request!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = User_Trip_Booking.objects.create(
            user_id=user_id,
            trip_id=trip_inst,
            trip_ammount=trip_amount,
            no_guests=no_guests,
        )
        users_inst.save()

        users_data = serializers.UserTripBookingSerializer(
            User_Trip_Booking.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)
        book_id = request.GET.get("book_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_post_inst = User_Trip_Booking.objects.filter(id=pk)
            scm_post_inst.delete()
            return Response(
                {"message": "Trip Booking Removed Successfully"},
                status=status.HTTP_200_OK,
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)


class TripPaymentViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_trip_booking = User_Trips_Payment.objects.filter(user=user_id)
            trip_booking_data_dic = serializers.UserTripsPaymentSerializer(
                sm_trip_booking, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(trip_booking_data_dic.data)):
            created_user_id = trip_booking_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                trip_booking_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                trip_booking_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_trip_booking_id = trip_booking_data_dic.data[i].get("trip_booking")
            try:
                trip_booking_inst = User_Trip_Booking.objects.get(
                    id=created_trip_booking_id
                )

                trip_booking_data_dic.data[i].update(
                    {
                        "trip_booking": {
                            "id": trip_booking_inst.id,
                            # "trip_id":trip_booking_inst.trip_id,
                            "no_guests": trip_booking_inst.no_guests,
                            "trip_ammount": trip_booking_inst.trip_ammount,
                            "trip_cart_status": trip_booking_inst.trip_cart_status,
                        }
                    }
                )
            except:
                trip_booking_data_dic.data[i].update(
                    {
                        "trip_booking": {
                            "id": created_trip_booking_id,
                            "message": "Deleted Trip Booking",
                        }
                    }
                )

        return Response(trip_booking_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        trip_booking = request.POST.get("trip_booking", None)
        payment_id = request.POST.get("payment_id", None)
        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            trip_booking_inst = User_Trip_Booking.objects.get(id=trip_booking)
        except:

            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = User_Trips_Payment.objects.create(
            user=user_inst,
            trip_booking=trip_booking_inst,
            payment_id=payment_id,
        )
        users_inst.save()

        users_data = serializers.UserTripsPaymentSerializer(
            User_Trips_Payment.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)


###########"""" TOUR GUIDE """"""#######
class UserTripsBookingViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_hotel = User_Guide_Booking.objects.filter(user=user_id)
            account_data_dic = serializers.UserGuideBookingSerializer(
                sm_hotel, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for i in range(0, len(account_data_dic.data)):
            created_user_id = account_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                account_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_name": user_inst.name,
                            "user_mobile": user_inst.mobile,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted User"}}
                )
            created_user_id = account_data_dic.data[i].get("client_id")
            try:
                user_inst = User_Register.objects.get(id=created_user_id)

                account_data_dic.data[i].update(
                    {
                        "client_id": {
                            "id": user_inst.id,
                            "client_name": user_inst.name,
                            "client_email": user_inst.email,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {"client_id": {"id": created_user_id, "message": "Deleted Clients"}}
                )
            created_user_id = account_data_dic.data[i].get("guide_id")
            try:
                user_inst = TourGuide_Reg.objects.get(id=created_user_id)

                account_data_dic.data[i].update(
                    {
                        "guide_id": {
                            "id": user_inst.id,
                            "guider_name":user_inst.guider_name,
                            "guider_mobile":user_inst.guider_mobile,
                            "rating":user_inst.rating,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {"guide_id": {"id": created_user_id, "message": "Deleted Guide"}}
                )
        return Response(account_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):
    
        user_id = request.POST.get("user_id", None)
        client_id = request.POST.get("client_id", None)
        guide_id = request.POST.get("guide_id", None)
        no_guests = request.POST.get("no_guests", None)
        guide_amount = request.POST.get("guide_amount", None)
        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            clients_inst = User_Register.objects.get(id=client_id)
            guide_inst = TourGuide_Reg.objects.get(id=guide_id)
        except:

            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = User_Guide_Booking.objects.create(
            user=user_inst,
            client_id=clients_inst,
            guide_id=guide_inst,
            no_guests=no_guests,
            guide_amount=guide_amount,
        )
        users_inst.save()

        users_data = serializers.UserGuideBookingSerializer(
            User_Guide_Booking.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

##############"""""""""""""" ADMIN """"""""""""""""""""###########


class GetAllUsersViewSet(viewsets.ViewSet):
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


class GetUsersHotelCartViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_hotel = User_Hotel_Cart.objects.all()
            hotel_data_dic = serializers.HotelCartSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(hotel_data_dic.data)):
            created_user_id = hotel_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                hotel_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_hotel_id = hotel_data_dic.data[i].get("hotel_id")
            try:
                hotel_inst = Reg_Hotel.objects.get(id=created_hotel_id)

                hotel_data_dic.data[i].update(
                    {
                        "hotel_id": {
                            "id": hotel_inst.id,
                            "hotel_code": hotel_inst.hotel_code,
                            "hotel_name": hotel_inst.hotel_name,
                            "geo_location": hotel_inst.geo_location,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {
                        "hotel_id": {
                            "id": created_hotel_id,
                            "message": "Deleted Hotel",
                        }
                    }
                )
            created_room_id = hotel_data_dic.data[i].get("room_id")
            try:
                room_inst = Room_Register.objects.get(id=created_room_id)

                hotel_data_dic.data[i].update(
                    {
                        "room_id": {
                            "id": room_inst.id,
                            "room_id": room_inst.room_id,
                            "room_type": room_inst.room_type,
                            "bed_type": room_inst.bed_type,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {
                        "room_id": {
                            "id": created_room_id,
                            "message": "Deleted room",
                        }
                    }
                )

        return Response(hotel_data_dic.data, status=status.HTTP_200_OK)


class GetUsersHotelBookingViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_hotel = User_Hotel_Booking.objects.all()
            hotel_data_dic = serializers.HotelBookingSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(hotel_data_dic.data)):
            created_user_id = hotel_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                hotel_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_hotel_id = hotel_data_dic.data[i].get("hotel_id")
            try:
                hotel_inst = Reg_Hotel.objects.get(id=created_hotel_id)

                hotel_data_dic.data[i].update(
                    {
                        "hotel_id": {
                            "id": hotel_inst.id,
                            "hotel_code": hotel_inst.hotel_code,
                            "hotel_name": hotel_inst.hotel_name,
                            "geo_location": hotel_inst.geo_location,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {
                        "hotel_id": {
                            "id": created_hotel_id,
                            "message": "Deleted Hotel",
                        }
                    }
                )
            created_room_id = hotel_data_dic.data[i].get("room_id")
            try:
                room_inst = Room_Register.objects.get(id=created_room_id)

                hotel_data_dic.data[i].update(
                    {
                        "room_id": {
                            "id": room_inst.id,
                            "room_id": room_inst.room_id,
                            "room_type": room_inst.room_type,
                            "bed_type": room_inst.bed_type,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {
                        "room_id": {
                            "id": created_room_id,
                            "message": "Deleted room",
                        }
                    }
                )

        return Response(hotel_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        book_id = request.POST.get("book_id", None)
        booking_status = request.POST.get("status", None)

        if pk is None:
            return Response(
                {"message": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = User_Hotel_Booking.objects.get(id=pk)
            post_inst.booking_status = booking_status
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Hotel Booking Updated Sucessfully"},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetUsersHotelPaymentViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_hotel = User_Hotel_Payment.objects.all()
            hotel_data_dic = serializers.UserHotelPaymentSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(hotel_data_dic.data)):
            created_user_id = hotel_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                hotel_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_hotel_id = hotel_data_dic.data[i].get("hotel_booking")
            try:
                hotel_inst = User_Hotel_Booking.objects.get(id=created_hotel_id)

                hotel_data_dic.data[i].update(
                    {
                        "hotel_booking": {
                            "id": hotel_inst.id,
                            # "hotel_id": hotel_inst.hotel_id,
                            # "room_id":hotel_inst.room_id,
                            "hotel_bookid": hotel_inst.hotel_bookid,
                            "check_in_date": hotel_inst.check_in_date,
                            "check_in_time": hotel_inst.check_in_time,
                            "check_out_date": hotel_inst.check_out_date,
                            "check_out_time": hotel_inst.check_out_time,
                            "guest_no": hotel_inst.guest_no,
                            "rooms": hotel_inst.rooms,
                            "amount_booking": hotel_inst.amount_booking,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {
                        "hotel_booking": {
                            "id": created_hotel_id,
                            "message": "Deleted Hotel Booking",
                        }
                    }
                )

        return Response(hotel_data_dic.data, status=status.HTTP_200_OK)


class GetUsersCabCartViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_hotel = User_Cab_Cart.objects.all()
            cabs_data_dic = serializers.CabCartSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(cabs_data_dic.data)):
            created_user_id = cabs_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                cabs_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_cab_id = cabs_data_dic.data[i].get("car_id")
            try:
                cab_inst = Cabs_Reg.objects.get(id=created_cab_id)

                cabs_data_dic.data[i].update(
                    {
                        "car_id": {
                            "id": cab_inst.id,
                            "car_code": cab_inst.car_code,
                            "car_name": cab_inst.car_name,
                            "vehicle_no": cab_inst.vehicle_no,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {
                        "car_id": {
                            "id": created_cab_id,
                            "message": "Deleted cab",
                        }
                    }
                )
            created_driver_id = cabs_data_dic.data[i].get("driver_id")
            try:
                driver_inst = Driver_Reg.objects.get(id=created_driver_id)

                cabs_data_dic.data[i].update(
                    {
                        "driver_id": {
                            "id": driver_inst.id,
                            "driver_name": driver_inst.driver_name,
                            "driver_mobile": driver_inst.driver_mobile,
                            "driver_email": driver_inst.driver_email,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {
                        "driver_id": {
                            "id": created_driver_id,
                            "message": "Deleted Driver",
                        }
                    }
                )
        return Response(cabs_data_dic.data, status=status.HTTP_200_OK)


class GetUsersCabBookingViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_hotel = User_Cab_Booking.objects.all()
            cabs_data_dic = serializers.CabBookingSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(cabs_data_dic.data)):
            created_user_id = cabs_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                cabs_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_cab_id = cabs_data_dic.data[i].get("car_id")
            try:
                cab_inst = Cabs_Reg.objects.get(id=created_cab_id)

                cabs_data_dic.data[i].update(
                    {
                        "car_id": {
                            "id": cab_inst.id,
                            "car_code": cab_inst.car_code,
                            "car_name": cab_inst.car_name,
                            "vehicle_no": cab_inst.vehicle_no,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {
                        "car_id": {
                            "id": created_cab_id,
                            "message": "Deleted cab",
                        }
                    }
                )
            created_driver_id = cabs_data_dic.data[i].get("driver_id")
            try:
                driver_inst = Driver_Reg.objects.get(id=created_driver_id)

                cabs_data_dic.data[i].update(
                    {
                        "driver_id": {
                            "id": driver_inst.id,
                            "driver_name": driver_inst.driver_name,
                            "driver_mobile": driver_inst.driver_mobile,
                            "driver_email": driver_inst.driver_email,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {
                        "driver_id": {
                            "id": created_driver_id,
                            "message": "Deleted Driver",
                        }
                    }
                )
        return Response(cabs_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        book_id = request.POST.get("book_id", None)
        booking_status = request.POST.get("status", None)

        if pk is None:
            return Response(
                {"message": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = User_Cab_Booking.objects.get(id=pk)
            post_inst.booking_status = booking_status
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Cab Booking Updated Sucessfully"},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetAllCabPaymentViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_cab_booking = User_Cab_Payment.objects.all()
            cab_booking_data_dic = serializers.UserCabPaymentSerializer(
                sm_cab_booking, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(cab_booking_data_dic.data)):
            created_user_id = cab_booking_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                cab_booking_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                cab_booking_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_cab_booking_id = cab_booking_data_dic.data[i].get("cab_booking")
            try:
                cab_booking_inst = User_Cab_Booking.objects.get(
                    id=created_cab_booking_id
                )

                cab_booking_data_dic.data[i].update(
                    {
                        "cab_booking": {
                            "id": cab_booking_inst.id,
                            "cab_bookid": cab_booking_inst.cab_bookid,
                            # "car_id":cab_booking_inst.car_id,
                            # "driver_id":cab_booking_inst.driver_id,
                            "check_in_date": cab_booking_inst.check_in_date,
                            "check_in_time": cab_booking_inst.check_in_time,
                            "check_out_date": cab_booking_inst.check_out_date,
                            "check_out_time": cab_booking_inst.check_out_time,
                            "end_trip": cab_booking_inst.end_trip,
                            "amount_booking": cab_booking_inst.amount_booking,
                            "no_guests": cab_booking_inst.no_guests,
                        }
                    }
                )
            except:
                cab_booking_data_dic.data[i].update(
                    {
                        "cab_booking": {
                            "id": created_cab_booking_id,
                            "message": "Deleted Cab Booking",
                        }
                    }
                )

        return Response(cab_booking_data_dic.data, status=status.HTTP_200_OK)


class GetAllTripPaymentViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_trip_booking = User_Trips_Payment.objects.all()
            trip_booking_data_dic = serializers.UserTripsPaymentSerializer(
                sm_trip_booking, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(trip_booking_data_dic.data)):
            created_user_id = trip_booking_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                trip_booking_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                trip_booking_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_trip_booking_id = trip_booking_data_dic.data[i].get("trip_booking")
            try:
                trip_booking_inst = User_Trip_Booking.objects.get(
                    id=created_trip_booking_id
                )

                trip_booking_data_dic.data[i].update(
                    {
                        "trip_booking": {
                            "id": trip_booking_inst.id,
                            # "trip_id":trip_booking_inst.trip_id,
                            "no_guests": trip_booking_inst.no_guests,
                            "trip_ammount": trip_booking_inst.trip_ammount,
                            "trip_cart_status": trip_booking_inst.trip_cart_status,
                        }
                    }
                )
            except:
                trip_booking_data_dic.data[i].update(
                    {
                        "trip_booking": {
                            "id": created_trip_booking_id,
                            "message": "Deleted Trip Booking",
                        }
                    }
                )

        return Response(trip_booking_data_dic.data, status=status.HTTP_200_OK)


class UserAllTripsBookingViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_hotel = User_Trip_Booking.objects.all()
            account_data_dic = serializers.UserTripBookingSerializer(
                sm_hotel, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for i in range(0, len(account_data_dic.data)):
            created_user_id = account_data_dic.data[i].get("trip_id")
            try:
                user_inst = My_Trips.objects.get(id=created_user_id)

                account_data_dic.data[i].update(
                    {
                        "trip_id": {
                            "id": user_inst.id,
                            "trip_title": user_inst.title,
                            "trip_category": user_inst.category,
                            "trip_price": user_inst.price,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {"trip_id": {"id": created_user_id, "message": "Deleted Trip"}}
                )

        return Response(account_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        book_id = request.POST.get("book_id", None)
        trip_cart_status = request.POST.get("status", None)

        if pk is None:
            return Response(
                {"message": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = User_Trip_Booking.objects.get(id=pk)
            post_inst.trip_cart_status = trip_cart_status
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Trip Booking Updated Sucessfully"},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetUserTripsCartViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_hotel = User_Trip_Cart.objects.all()
            account_data_dic = serializers.UserTripCartSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for i in range(0, len(account_data_dic.data)):
            created_user_id = account_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                account_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_name": user_inst.name,
                            "user_mobile": user_inst.mobile,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Trip"}}
                )
            created_user_id = account_data_dic.data[i].get("trip_id")
            try:
                user_inst = My_Trips.objects.get(id=created_user_id)

                account_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "trip_title": user_inst.title,
                            "trip_category": user_inst.category,
                            "trip_price": user_inst.price,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )

        return Response(account_data_dic.data, status=status.HTTP_200_OK)


########"""""""" USERS BOOKINGS""""""""########


class GetMyUsersHotelBookingViewSet(viewsets.ViewSet):
    def list(self, request):
        client_id = request.GET.get("client_id", None)
        try:
            sm_hotel = User_Hotel_Booking.objects.filter(user_ip=client_id)
            hotel_data_dic = serializers.HotelBookingSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(hotel_data_dic.data)):
            created_user_id = hotel_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                hotel_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                            "user_mobile": user_inst.mobile,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_hotel_id = hotel_data_dic.data[i].get("hotel_id")
            try:
                hotel_inst = Reg_Hotel.objects.get(id=created_hotel_id)

                hotel_data_dic.data[i].update(
                    {
                        "hotel_id": {
                            "id": hotel_inst.id,
                            "hotel_code": hotel_inst.hotel_code,
                            "hotel_name": hotel_inst.hotel_name,
                            "geo_location": hotel_inst.geo_location,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {
                        "hotel_id": {
                            "id": created_hotel_id,
                            "message": "Deleted Hotel",
                        }
                    }
                )
            created_room_id = hotel_data_dic.data[i].get("room_id")
            try:
                room_inst = Room_Register.objects.get(id=created_room_id)

                hotel_data_dic.data[i].update(
                    {
                        "room_id": {
                            "id": room_inst.id,
                            "room_id": room_inst.room_id,
                            "room_type": room_inst.room_type,
                            "bed_type": room_inst.bed_type,
                        }
                    }
                )
            except:
                hotel_data_dic.data[i].update(
                    {
                        "room_id": {
                            "id": created_room_id,
                            "message": "Deleted room",
                        }
                    }
                )

        return Response(hotel_data_dic.data, status=status.HTTP_200_OK)


class GetMyUsersCabBookingViewSet(viewsets.ViewSet):
    def list(self, request):
        client_id = request.GET.get("client_id", None)
        try:
            sm_hotel = User_Cab_Booking.objects.filter(user_ip=client_id)
            cabs_data_dic = serializers.CabBookingSerializer(sm_hotel, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(cabs_data_dic.data)):
            created_user_id = cabs_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                cabs_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                            "user_mobile": user_inst.mobile,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_cab_id = cabs_data_dic.data[i].get("car_id")
            try:
                cab_inst = Cabs_Reg.objects.get(id=created_cab_id)

                cabs_data_dic.data[i].update(
                    {
                        "car_id": {
                            "id": cab_inst.id,
                            "car_code": cab_inst.car_code,
                            "car_name": cab_inst.car_name,
                            "vehicle_no": cab_inst.vehicle_no,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {
                        "car_id": {
                            "id": created_cab_id,
                            "message": "Deleted cab",
                        }
                    }
                )
            created_driver_id = cabs_data_dic.data[i].get("driver_id")
            try:
                driver_inst = Driver_Reg.objects.get(id=created_driver_id)

                cabs_data_dic.data[i].update(
                    {
                        "driver_id": {
                            "id": driver_inst.id,
                            "driver_name": driver_inst.driver_name,
                            "driver_mobile": driver_inst.driver_mobile,
                            "driver_email": driver_inst.driver_email,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {
                        "driver_id": {
                            "id": created_driver_id,
                            "message": "Deleted Driver",
                        }
                    }
                )
        return Response(cabs_data_dic.data, status=status.HTTP_200_OK)

        # def update(self, request, pk=None):
        # pk = tokenConversion(request)
        # description = request.GET.get("description", None)

        # if pk is None:
        #     return Response(
        #         {"message": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST
        #     )

        # try:
        #     post_inst = SocialMediaPost.objects.get(id=pk)
        #     post_inst.description = description
        #     post_inst.is_edited = True
        #     post_inst.save()

        #     return Response(
        #         {"message": "Post Updated Sucessfully", "data": post_data.data},
        #         status=status.HTTP_200_OK,
        #     )

        # except:
        #     return Response(
        #         {"message": "Sorry No data found with this post id"},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )

        # def destroy(self, request, pk=None):
        # pk = tokenConversion(request)
        # post_id = request.GET.get("post_id", None)

        # if pk is None:
        #     return Response(
        #         {"message": "Please provide user_id"},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )
        # try:
        #     scm_post_inst = SocialMediaPost.objects.get(id=post_id)
        #     scm_post_dic = serializers.SocialMediaPostSerializer(scm_post_inst)
        #     user_inst = user_details.objects.get(id=pk)
        #     scm_post_inst.likes.remove(user_inst)
        #     return Response(
        #         {"message": "Successfully unliked"}, status=status.HTTP_200_OK
        #     )
        # except:
        #     return Response({"message": "Details not found"}, status=status.HTTP_200_OK)
