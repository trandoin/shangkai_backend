from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets
from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail
import random

from . import serializers

# Create your views here.
"""Model Package """
from .models import (
    Reg_Hotel,
    Tour_Packages,
    Tour_locations,
    TourGuide_Reg,
    User_Register,
    Room_Register,
    Driver_Reg,
    Cabs_Reg,
    Client_login,
)

from shangkai_app.models import (
    Hotel_Category,
)


class UserRegisterViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.POST.get("user_id", None)
        try:
            sm_users = User_Register.objects.filter(id=user_id)
            users_data_dic = serializers.UserRegisterSerializer(sm_users, many=True)
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
        otp = random.randint(1111, 9999)

        users_inst = User_Register.objects.create(
            user_id=user_id,
            user_ip=user_ip,
            name=name,
            email=email,
            mobile=mobile,
            password=password,
            otp=otp,
            image=image,
        )
        users_inst.save()

        subject = 'Team Shangkai : Account verification'
        message = f'Dear, {users_inst.name}, Your verification url is : https://shangkai.in/verify/clients.php?email={email}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [users_inst.email, ]
        send_mail( subject, message, email_from, recipient_list )

        users_data = serializers.UserRegisterSerializer(
            User_Register.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        name = request.POST.get("name", None)
        mobile = request.POST.get("mobile", None)
        password = request.POST.get("password", None)
        address = request.POST.get("address", None)
        city = request.POST.get("city", None)
        state = request.POST.get("state", None)
        pin_code = request.POST.get("pin_code", None)
        voter_id = request.POST.get("voter_id", None)
        whatsapp_no = request.POST.get("whatsapp_no", None)
        emergency_no = request.POST.get("emergency_no", None)
        bank_name = request.POST.get("bank_name", None)
        bank_branch = request.POST.get("bank_branch", None)
        account_no = request.POST.get("account_no", None)
        ifsc_code = request.POST.get("ifsc_code", None)
        image = request.POST.get("image", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = User_Register.objects.get(id=pk)
            post_inst.name = name
            post_inst.mobile = mobile
            post_inst.password = password
            post_inst.address = address
            post_inst.city = city
            post_inst.state = state
            post_inst.pin_code = pin_code
            post_inst.voter_id = voter_id
            post_inst.whatsapp_no = whatsapp_no
            post_inst.emergency_no = emergency_no
            post_inst.bank_name = bank_name
            post_inst.bank_branch = bank_branch
            post_inst.account_no = account_no
            post_inst.ifsc_code = ifsc_code
            post_inst.image = image
            post_inst.is_edited = True
            post_inst.save()

            users_data = serializers.UserRegisterSerializer(
                User_Register.objects.filter(id=post_inst.id), many=True
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


class ClientsUpdatePasswordViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.POST.get("user_id", None)
        try:
            sm_users = User_Register.objects.filter(id=user_id)
            users_data_dic = serializers.UserRegisterSerializer(sm_users, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)
    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        password = request.POST.get("password", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = User_Register.objects.get(id=pk)
            post_inst.password = password
            post_inst.is_edited = True
            post_inst.save()

            users_data = serializers.UserRegisterSerializer(
                User_Register.objects.filter(id=post_inst.id), many=True
            )
            return Response(
                {"message": "Password Updated successfully !"},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ClientVerifyOTPViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_users = User_Register.objects.filter(id=user_id)
            users_data_dic = serializers.UserRegisterSerializer(
                sm_users, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_email = request.POST.get("user_email", None)
        otp = request.POST.get("otp", None)
        status = 1

        if otp is None:
            return Response(
                {"message": "Enter OTP !"}
            )

        try:
            users_inst = User_Register.objects.filter(email=user_email, otp=otp)
            users_data_dic = serializers.UserRegisterSerializer(
                users_inst, many=True
            )
            user_inst = User_Register.objects.get(id=pk)
            user_inst.status = status
            user_inst.is_edited = True
            user_inst.save()
  
        except:
            return Response(
                {"message": "Invalid OTP !"}
            )
        return Response(
                {"message": "OTP Verified !"}
            ) 


class ClientloginViewSet(viewsets.ViewSet):
    def create(self, request):

        email = request.POST.get("email", None)
        password = request.POST.get("password", None)

        if email is None and password is None:

            return Response(
                {"message": "Enter username & password !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            users_inst = User_Register.objects.filter(email=email, password=password)
            users_data_dic = serializers.UserRegisterSerializer(users_inst, many=True)
        except:
            return Response(
                {"message": "Invalid username & password !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)


class HotelRegistrationViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_users = Reg_Hotel.objects.filter(user=user_id)
            users_data_dic = serializers.HotelRegisterSerializer(sm_users, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(users_data_dic.data)):
            created_user_id = users_data_dic.data[i].get("user")
            try:
                user_inst = User_Register.objects.get(id=created_user_id)

                users_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                users_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        hotel_code = request.POST.get("hotel_code", None)
        hotel_cat = request.POST.get("hotel_cat", None)
        hotel_name = request.POST.get("hotel_name", None)
        hotel_address = request.POST.get("hotel_address", None)
        hotel_city = request.POST.get("hotel_city", None)
        hotel_state = request.POST.get("hotel_state", None)
        geo_location = request.POST.get("geo_location", None)
        pin_code = request.POST.get("pin_code", None)
        room_rates = request.POST.get("room_rates", None)
        hotel_facilites = request.POST.get("hotel_facilites", None)
        max_guests_limit = request.POST.get("max_guests_limit", None)
        hotel_images = request.POST.get("hotel_images", None)

        try:
            user_inst = User_Register.objects.get(id=user_id)
            hotel_cat_inst = Hotel_Category.objects.get(id=hotel_cat)

        except:

            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        users_inst = Reg_Hotel.objects.create(
            user=user_inst,
            hotel_cat=hotel_cat_inst,
            hotel_code=hotel_code,
            hotel_name=hotel_name,
            hotel_address=hotel_address,
            hotel_city=hotel_city,
            hotel_state=hotel_state,
            geo_location=geo_location,
            pin_code=pin_code,
            room_rates=room_rates,
            hotel_facilites=hotel_facilites,
            max_guests_limit=max_guests_limit,
            hotel_images=hotel_images,
        )
        users_inst.save()

        users_data = serializers.HotelRegisterSerializer(
            Reg_Hotel.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        hotel_name = request.POST.get("hotel_name", None)
        hotel_address = request.POST.get("hotel_address", None)
        hotel_city = request.POST.get("hotel_city", None)
        hotel_state = request.POST.get("hotel_state", None)
        geo_location = request.POST.get("geo_location", None)
        pin_code = request.POST.get("pin_code", None)
        room_rates = request.POST.get("room_rates", None)
        hotel_facilites = request.POST.get("hotel_facilites", None)
        max_guests_limit = request.POST.get("max_guests_limit", None)
        hotel_images = request.POST.get("hotel_images", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = Reg_Hotel.objects.get(id=pk)
            post_inst.hotel_name = hotel_name
            post_inst.hotel_address = hotel_address
            post_inst.hotel_city = hotel_city
            post_inst.hotel_state = hotel_state
            post_inst.geo_location = geo_location
            post_inst.pin_code = pin_code
            post_inst.room_rates = room_rates
            post_inst.hotel_facilites = hotel_facilites
            post_inst.max_guests_limit = max_guests_limit
            post_inst.hotel_images = hotel_images
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Hotel Updated Sucessfully"},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)
        hotel_id = request.GET.get("hotel_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_post_inst = Reg_Hotel.objects.filter(id=pk)
            scm_post_inst.delete()
            return Response(
                {"message": "Hotel Deleted Successfully"}, status=status.HTTP_200_OK
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)


class RoomRegistrationViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        # hotel_id = request.POST.get("hotel_id", None)

        try:
            sm_users = Room_Register.objects.filter(user=user_id)
            users_data_dic = serializers.RoomRegisterSerializer(sm_users, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(users_data_dic.data)):
            created_user_id = users_data_dic.data[i].get("user")
            try:
                user_inst = User_Register.objects.get(id=created_user_id)

                users_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                users_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )
            created_hotel_id = users_data_dic.data[i].get("hotel_id")
            try:
                hotel_inst = Reg_Hotel.objects.get(id=created_hotel_id)

                users_data_dic.data[i].update(
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
                users_data_dic.data[i].update(
                    {
                        "hotel_id": {
                            "id": created_hotel_id,
                            "message": "Deleted Hotel",
                        }
                    }
                )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        hotel_id = request.POST.get("hotel_id", None)
        room_id = request.POST.get("room_id", None)
        room_type = request.POST.get("room_type", None)
        bed_type = request.POST.get("bed_type", None)
        totel_beds = request.POST.get("totel_beds", None)
        room_rates = request.POST.get("room_rates", None)
        room_facilites = request.POST.get("room_facilites", None)
        max_guests_limit = request.POST.get("max_guests_limit", None)
        no_rooms = request.POST.get("no_rooms", None)
        rating = request.POST.get("rating", None)
        tags = request.POST.get("tags", None)
        extra_services = request.POST.get("extra_services", None)
        room_images = request.POST.get("room_images", None)

        try:
            user_inst = User_Register.objects.get(id=user_id)
            hotel_inst = Reg_Hotel.objects.get(id=hotel_id)
        except:

            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        users_inst = Room_Register.objects.create(
            user=user_inst,
            hotel_id=hotel_inst,
            room_id=room_id,
            room_type=room_type,
            bed_type=bed_type,
            totel_beds=totel_beds,
            room_rates=room_rates,
            room_facilites=room_facilites,
            max_guests_limit=max_guests_limit,
            no_rooms=no_rooms,
            tags=tags,
            rating=rating,
            extra_services=extra_services,
            room_images=room_images,
        )
        users_inst.save()

        users_data = serializers.RoomRegisterSerializer(
            Room_Register.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        room_type = request.POST.get("room_type", None)
        bed_type = request.POST.get("bed_type", None)
        totel_beds = request.POST.get("totel_beds", None)
        room_rates = request.POST.get("room_rates", None)
        room_facilites = request.POST.get("room_facilites", None)
        max_guests_limit = request.POST.get("max_guests_limit", None)
        no_rooms = request.POST.get("no_rooms", None)
        rating = request.POST.get("rating", None)
        tags = request.POST.get("tags", None)
        extra_services = request.POST.get("extra_services", None)
        room_images = request.POST.get("room_images", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = Room_Register.objects.get(id=pk)
            post_inst.room_type = room_type
            post_inst.bed_type = bed_type
            post_inst.totel_beds = totel_beds
            post_inst.room_rates = room_rates
            post_inst.room_facilites = room_facilites
            post_inst.max_guests_limit = max_guests_limit
            post_inst.no_rooms = no_rooms
            post_inst.tags = tags
            post_inst.extra_services = extra_services
            post_inst.room_images = room_images
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Room details Updated Sucessfully"},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)
        room_id = request.GET.get("room_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_post_inst = Room_Register.objects.filter(id=pk)
            scm_post_inst.delete()
            return Response(
                {"message": "Room Deleted Successfully"}, status=status.HTTP_200_OK
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)


class DriverRegistrationViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_driver = Driver_Reg.objects.filter(user=user_id)
            driver_data_dic = serializers.DriverRegisterSerializer(sm_driver, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(driver_data_dic.data)):
            created_user_id = driver_data_dic.data[i].get("user")
            try:
                user_inst = User_Register.objects.get(id=created_user_id)

                driver_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                driver_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )

        return Response(driver_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        driver_id = request.POST.get("driver_id", None)
        driver_name = request.POST.get("driver_name", None)
        driver_address = request.POST.get("driver_address", None)
        driver_mobile = request.POST.get("driver_mobile", None)
        driver_email = request.POST.get("driver_email", None)
        languages = request.POST.get("languages", None)
        working_hours = request.POST.get("room_facilites", None)
        licence_no = request.POST.get("licence_no", None)
        adhar_card = request.POST.get("adhar_card", None)
        licence_doc = request.POST.get("licence_doc", None)
        picture = request.POST.get("picture", None)

        try:
            user_inst = User_Register.objects.get(id=user_id)
        except:

            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        users_inst = Driver_Reg.objects.create(
            user=user_inst,
            driver_id=driver_id,
            driver_name=driver_name,
            driver_address=driver_address,
            driver_mobile=driver_mobile,
            driver_email=driver_email,
            languages=languages,
            working_hours=working_hours,
            licence_no=licence_no,
            adhar_card=adhar_card,
            licence_doc=licence_doc,
            picture=picture,
        )
        users_inst.save()

        users_data = serializers.DriverRegisterSerializer(
            Driver_Reg.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        driver_name = request.POST.get("driver_name", None)
        driver_address = request.POST.get("driver_address", None)
        driver_mobile = request.POST.get("driver_mobile", None)
        driver_email = request.POST.get("driver_email", None)
        languages = request.POST.get("languages", None)
        working_hours = request.POST.get("room_facilites", None)
        licence_no = request.POST.get("licence_no", None)
        adhar_card = request.POST.get("adhar_card", None)
        licence_doc = request.POST.get("licence_doc", None)
        picture = request.POST.get("picture", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = Driver_Reg.objects.get(id=pk)
            post_inst.driver_name = driver_name
            post_inst.driver_address = driver_address
            post_inst.driver_mobile = driver_mobile
            post_inst.driver_email = driver_email
            post_inst.languages = languages
            post_inst.working_hours = working_hours
            post_inst.licence_no = licence_no
            post_inst.adhar_card = adhar_card
            post_inst.licence_doc = licence_doc
            post_inst.picture = picture
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Driver details Updated Sucessfully"},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)
        driver_id = request.GET.get("driver_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_post_inst = Driver_Reg.objects.filter(id=pk)
            scm_post_inst.delete()
            return Response(
                {"message": "Driver Deleted Successfully"}, status=status.HTTP_200_OK
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)


class CabRegistrationViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_cabs = Cabs_Reg.objects.filter(user=user_id)
            cabs_data_dic = serializers.CabRegisterSerializer(sm_cabs, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(cabs_data_dic.data)):
            created_user_id = cabs_data_dic.data[i].get("user")
            try:
                user_inst = User_Register.objects.get(id=created_user_id)

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
            created_driver = cabs_data_dic.data[i].get("driver")
            try:
                hotel_inst = Driver_Reg.objects.get(id=created_driver)

                cabs_data_dic.data[i].update(
                    {
                        "driver": {
                            "id": hotel_inst.id,
                            "driver_id": hotel_inst.driver_id,
                            "driver_name": hotel_inst.driver_name,
                            "driver_mobile": hotel_inst.driver_mobile,
                        }
                    }
                )
            except:
                cabs_data_dic.data[i].update(
                    {
                        "driver": {
                            "id": created_driver,
                            "message": "Deleted ",
                        }
                    }
                )
        return Response(cabs_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        driver_id = request.POST.get("driver_id", None)
        car_code = request.POST.get("car_code", None)
        car_name = request.POST.get("car_name", None)
        car_type = request.POST.get("car_type", None)
        capacity = request.POST.get("capacity", None)
        vehicle_no = request.POST.get("vehicle_no", None)
        car_mou = request.POST.get("room_facilites", None)
        car_fee = request.POST.get("car_fee", None)
        pickup_point = request.POST.get("pickup_point", None)
        destination = request.POST.get("destination", None)
        checkin_date = request.POST.get("checkin_date", None)
        checkout_date = request.POST.get("checkout_date", None)
        car_rating = request.POST.get("car_rating", None)
        car_rc = request.POST.get("car_rc", None)
        car_insurance = request.POST.get("car_insurance", None)
        car_images = request.POST.get("car_images", None)

        try:
            user_inst = User_Register.objects.get(id=user_id)
            driver_inst = Driver_Reg.objects.get(id=driver_id)
        except:

            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        users_inst = Cabs_Reg.objects.create(
            user=user_inst,
            driver=driver_inst,
            car_code=car_code,
            car_name=car_name,
            car_type=car_type,
            capacity=capacity,
            vehicle_no=vehicle_no,
            car_mou=car_mou,
            car_fee=car_fee,
            pickup_point=pickup_point,
            destination=destination,
            checkin_date=checkin_date,
            checkout_date=checkout_date,
            car_rating=car_rating,
            car_rc=car_rc,
            car_insurance=car_insurance,
            car_images=car_images,
        )
        users_inst.save()

        users_data = serializers.CabRegisterSerializer(
            Cabs_Reg.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        car_name = request.POST.get("car_name", None)
        car_type = request.POST.get("car_type", None)
        capacity = request.POST.get("capacity", None)
        vehicle_no = request.POST.get("vehicle_no", None)
        car_mou = request.POST.get("room_facilites", None)
        car_fee = request.POST.get("car_fee", None)
        pickup_point = request.POST.get("pickup_point", None)
        destination = request.POST.get("destination", None)
        checkin_date = request.POST.get("checkin_date", None)
        checkout_date = request.POST.get("checkout_date", None)
        car_rc = request.POST.get("car_rc", None)
        car_insurance = request.POST.get("car_insurance", None)
        car_images = request.POST.get("car_images", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = Cabs_Reg.objects.get(id=pk)
            post_inst.car_name = car_name
            post_inst.car_type = car_type
            post_inst.capacity = capacity
            post_inst.vehicle_no = vehicle_no
            post_inst.car_mou = car_mou
            post_inst.car_fee = car_fee
            post_inst.pickup_point = pickup_point
            post_inst.destination = destination
            post_inst.checkin_date = checkin_date
            post_inst.checkout_date = checkout_date
            post_inst.car_rc = car_rc
            post_inst.car_insurance = car_insurance
            post_inst.car_images = car_images
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Cab Details Updated Sucessfully"},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)
        cab_id = request.GET.get("cab_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_post_inst = Cabs_Reg.objects.filter(id=pk)
            scm_post_inst.delete()
            return Response(
                {"message": "Cab Deleted Successfully"}, status=status.HTTP_200_OK
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)

########### STATUS UPDATE ######################

### HOTEL 
class HotelUpdateStatusViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_users = Reg_Hotel.objects.filter(user=user_id)
            users_data_dic = serializers.HotelRegisterSerializer(sm_users, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"}
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        status = request.POST.get("status", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}
            )

        try:
            post_inst = Reg_Hotel.objects.get(id=pk)
            post_inst.status = status

            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Hotel Status Updated Sucessfully"}
            )

        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"}
            )        

###### ROOMS
class RoomsUpdateStatusViewSet(viewsets.ViewSet): 
    def list(self, request):
        user_id = request.GET.get("user_id", None)

        try:
            sm_users = Room_Register.objects.filter(user=user_id)
            users_data_dic = serializers.RoomRegisterSerializer(sm_users, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK) 

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        status = request.POST.get("status", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}
            )

        try:
            post_inst = Room_Register.objects.get(id=pk)
            post_inst.states = status
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Room Status Updated Sucessfully"}
            )

        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"}
            )        

###### CABS
class CabUpdateStatusViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_cabs = Cabs_Reg.objects.filter(user=user_id)
            cabs_data_dic = serializers.CabRegisterSerializer(sm_cabs, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"}
            )

        return Response(cabs_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        status = request.POST.get("status", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}
            )

        try:
            post_inst = Cabs_Reg.objects.get(id=pk)
            post_inst.status = status

            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Cab Status Updated Sucessfully"}
            )

        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"}
            )        

##### DRIVERS
class DriverUpdateStatusViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_driver = Driver_Reg.objects.filter(user=user_id)
            driver_data_dic = serializers.DriverRegisterSerializer(sm_driver, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"}
            )

        return Response(driver_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        status = request.POST.get("status", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}
            )

        try:
            post_inst = Driver_Reg.objects.get(id=pk)
            post_inst.status = status
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Driver Status Updated Sucessfully"}
            )

        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"}
            )        

###### TOUR LOCATIONS
class TourLocationsUpdateStatusViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_rooms = Tour_locations.objects.filter(user=user_id)
            room_data_dic = serializers.TourlocationsSerializer(sm_rooms, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"}
            )

        return Response(room_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        status = request.POST.get("status", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}
            )

        try:
            post_inst = Tour_locations.objects.get(id=pk)
            post_inst.status = status
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Tour Location Status Updated Sucessfully"}
            )

        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"}
            )        

###### TOUR PACKAGES
class TourPackagesUpdateStatusViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_rooms = Tour_Packages.objects.filter(user=user_id)
            room_data_dic = serializers.TourPackagesSerializer(sm_rooms, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"}
            )
        return Response(room_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        status = request.POST.get("status", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}
            )

        try:
            post_inst = Tour_Packages.objects.get(id=pk)
            post_inst.status = status
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Tour Package Status Updated Sucessfully"}
            )

        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"}
            )

###### TOUR GUIDE
class TourGuideUpdateStatusViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_rooms = TourGuide_Reg.objects.filter(user=user_id)
            tourguide_data_dic = serializers.TourGuideRegSerializer(sm_rooms, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(tourguide_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        status = request.POST.get("status", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}
            )

        try:
            post_inst = TourGuide_Reg.objects.get(id=pk)
            post_inst.status = status
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Tour Guider Status Updated Sucessfully"}
            )

        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"}
            )


###############      SEARCH BAR  #######################


class CabSearchViewSet(viewsets.ViewSet):
    def list(self, request):
        cab_name = request.GET.get("cab_name", None)
        checkin_date = request.GET.get("checkin_date", None)
        checkout_date = request.GET.get("checkout_date", None)
        from_location = request.GET.get("from_location", None)
        destination = request.GET.get("destination", None)
        try:
            sm_cabs = Cabs_Reg.objects.filter(
                car_name=cab_name,
                checkin_date=checkin_date,
                checkout_date=checkout_date,
                pickup_point=from_location,
                destination=destination,
            )
            cabs_data_dic = serializers.CabRegisterSerializer(sm_cabs, many=True)
        except:
            return Response(
                {"message": "Sorry No cab found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(cabs_data_dic.data, status=status.HTTP_200_OK)


class CabGetByLocationViewSet(viewsets.ViewSet):
    def list(self, request):
        from_location = request.GET.get("from_location", None)
        destination = request.GET.get("destination", None)
        try:
            sm_cabs = Cabs_Reg.objects.filter(
                pickup_point=from_location, destination=destination
            )
            cabs_data_dic = serializers.CabRegisterSerializer(sm_cabs, many=True)
        except:
            return Response(
                {"message": "Sorry No cab found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(cabs_data_dic.data, status=status.HTTP_200_OK)


class RoomSearchViewSet(viewsets.ViewSet):
    def list(self, request):
        hotel_city = request.GET.get("hotel_city", None)
        checkin_date = request.GET.get("checkin_date", None)
        checkout_date = request.GET.get("checkout_date", None)
        try:
            sm_rooms = Room_Register.objects.filter(
                checkin_date=checkin_date, checkout_date=checkout_date
            )
            room_data_dic = serializers.RoomRegisterSerializer(sm_rooms, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(room_data_dic.data)):
            created_hotel_id = room_data_dic.data[i].get("hotel_id")
            try:
                hotel_inst = Reg_Hotel.objects.get(id=created_hotel_id)

                room_data_dic.data[i].update(
                    {
                        "hotel_id": {
                            "id": hotel_inst.id,
                            "hotel_name": hotel_inst.hotel_name,
                            "hotel_city": hotel_inst.hotel_city,
                            "room_rates": hotel_inst.room_rates,
                        }
                    }
                )
            except:
                room_data_dic.data[i].update(
                    {"hotel_id": {"id": created_hotel_id, "message": "No Hotel found"}}
                )
        return Response(room_data_dic.data, status=status.HTTP_200_OK)


class RoomGetByIdViewSet(viewsets.ViewSet):
    def list(self, request):
        room_id = request.GET.get("room_id", None)
        try:
            sm_rooms = Room_Register.objects.filter(id=room_id)
            room_data_dic = serializers.RoomRegisterSerializer(sm_rooms, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(room_data_dic.data)):
            created_hotel_id = room_data_dic.data[i].get("hotel_id")
            try:
                hotel_inst = Reg_Hotel.objects.get(id=created_hotel_id)

                room_data_dic.data[i].update(
                    {
                        "hotel_id": {
                            "id": hotel_inst.id,
                            "hotel_name": hotel_inst.hotel_name,
                            "hotel_city": hotel_inst.hotel_city,
                            "room_rates": hotel_inst.room_rates,
                        }
                    }
                )
            except:
                room_data_dic.data[i].update(
                    {"hotel_id": {"id": created_hotel_id, "message": "No Hotel found"}}
                )

        return Response(room_data_dic.data, status=status.HTTP_200_OK)


class GetHotelByCatIdViewSet(viewsets.ViewSet):
    def list(self, request):
        hotel_cat_id = request.GET.get("hotel_cat_id", None)

        try:
            sm_users = Reg_Hotel.objects.filter(hotel_cat=hotel_cat_id)
            users_data_dic = serializers.HotelRegisterSerializer(sm_users, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)


############ """""" TOUR GUIDER """"""""##########


class TourLocationsViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_rooms = Tour_locations.objects.filter(user=user_id)
            room_data_dic = serializers.TourlocationsSerializer(sm_rooms, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(room_data_dic.data)):
            created_user = room_data_dic.data[i].get("user")
            try:
                package_inst = User_Register.objects.get(id=created_user)

                room_data_dic.data[i].update(
                    {
                        "user": {
                            "id": package_inst.id,
                            "name": package_inst.name,
                            "mobile": package_inst.mobile,
                        }
                    }
                )
            except:
                room_data_dic.data[i].update(
                    {
                        "user": {
                            "id": created_user,
                            "message": "Deleted user",
                        }
                    }
                )

        return Response(room_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        locations = request.POST.get("locations", None)
        location_image = request.POST.get("location_image", None)

        try:
            user_inst = User_Register.objects.get(id=user_id)
        except:

            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        location_inst = Tour_locations.objects.create(
            user=user_inst,
            locations=locations,
            location_image=location_image,
        )
        location_inst.save()

        location_data = serializers.TourlocationsSerializer(
            Tour_locations.objects.filter(id=location_inst.id), many=True
        )
        return Response(location_data.data[0], status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_location_inst = Tour_locations.objects.filter(id=pk)
            scm_location_inst.delete()
            return Response(
                {"message": "Tour Location deleted successfully"},
                status=status.HTTP_200_OK,
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)


class TourPackagesViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_rooms = Tour_Packages.objects.filter(user=user_id)
            room_data_dic = serializers.TourPackagesSerializer(sm_rooms, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(room_data_dic.data)):
            created_user = room_data_dic.data[i].get("user")
            try:
                package_inst = User_Register.objects.get(id=created_user)

                room_data_dic.data[i].update(
                    {
                        "user": {
                            "id": package_inst.id,
                            "name": package_inst.name,
                            "mobile": package_inst.mobile,
                        }
                    }
                )
            except:
                room_data_dic.data[i].update(
                    {
                        "user": {
                            "id": created_user,
                            "message": "Deleted user",
                        }
                    }
                )
        return Response(room_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        location_ids = request.POST.get("location_ids", None)
        package_amount = request.POST.get("package_amount", None)

        try:
            user_inst = User_Register.objects.get(id=user_id)
        except:

            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        package_inst = Tour_Packages.objects.create(
            user=user_inst,
            location_ids=location_ids,
            package_amount=package_amount,
        )
        package_inst.save()

        package_data = serializers.TourPackagesSerializer(
            Tour_Packages.objects.filter(id=package_inst.id), many=True
        )
        return Response(package_data.data[0], status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_package_inst = Tour_Packages.objects.filter(id=pk)
            scm_package_inst.delete()
            return Response(
                {"message": "Tour package deleted successfully"},
                status=status.HTTP_200_OK,
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)


class TourGuiderViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_rooms = TourGuide_Reg.objects.filter(user=user_id)
            tourguide_data_dic = serializers.TourGuideRegSerializer(sm_rooms, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(tourguide_data_dic.data)):
            created_user = tourguide_data_dic.data[i].get("user")
            try:
                package_inst = User_Register.objects.get(id=created_user)

                tourguide_data_dic.data[i].update(
                    {
                        "user": {
                            "id": package_inst.id,
                            "name": package_inst.name,
                            "mobile": package_inst.mobile,
                        }
                    }
                )
            except:
                tourguide_data_dic.data[i].update(
                    {
                        "user": {
                            "id": created_user,
                            "message": "Deleted user",
                        }
                    }
                )
            created_tour_locations = tourguide_data_dic.data[i].get("tour_locations")
            try:
                package_inst = Tour_locations.objects.get(id=created_tour_locations)

                tourguide_data_dic.data[i].update(
                    {
                        "tour_locations": {
                            "id": package_inst.id,
                            "locations": package_inst.locations,
                            "status": package_inst.status,
                        }
                    }
                )
            except:
                tourguide_data_dic.data[i].update(
                    {
                        "tour_locations": {
                            "id": created_tour_locations,
                            "message": "Deleted tour_locations",
                        }
                    }
                )
            created_packages = tourguide_data_dic.data[i].get("packages")
            try:
                package_inst = Tour_Packages.objects.get(id=created_packages)

                tourguide_data_dic.data[i].update(
                    {
                        "packages": {
                            "id": package_inst.id,
                            "location_ids": package_inst.location_ids,
                            "package_amount": package_inst.package_amount,
                        }
                    }
                )
            except:
                tourguide_data_dic.data[i].update(
                    {
                        "packages": {
                            "id": created_packages,
                            "message": "Deleted Packages",
                        }
                    }
                )

        return Response(tourguide_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        tour_locations = request.POST.get("tour_locations", None)
        packages = request.POST.get("packages", None)
        guider_name = request.POST.get("guider_name", None)
        about_guider = request.POST.get("about_guider", None)
        guider_address = request.POST.get("guider_address", None)
        guider_mobile = request.POST.get("guider_mobile", None)
        guider_email = request.POST.get("guider_email", None)
        languages = request.POST.get("languages", None)
        adhar_card = request.POST.get("adhar_card", None)
        licence_doc = request.POST.get("licence_doc", None)
        picture = request.POST.get("picture", None)

        try:
            user_inst = User_Register.objects.get(id=user_id)
            location_inst = Tour_locations.objects.get(id=tour_locations)
            packages_inst = Tour_Packages.objects.get(id=packages)
        except:

            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        guide_inst = TourGuide_Reg.objects.create(
            user=user_inst,
            tour_locations=location_inst,
            packages=packages_inst,
            guider_name=guider_name,
            about_guider=about_guider,
            guider_address=guider_address,
            guider_mobile=guider_mobile,
            guider_email=guider_email,
            languages=languages,
            adhar_card=adhar_card,
            licence_doc=licence_doc,
            picture=picture,
        )
        guide_inst.save()

        guide_data = serializers.TourGuideRegSerializer(
            TourGuide_Reg.objects.filter(id=guide_inst.id), many=True
        )
        return Response(guide_data.data[0], status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_tourguide_inst = TourGuide_Reg.objects.filter(id=pk)
            scm_tourguide_inst.delete()
            return Response(
                {"message": "Tour tour guider deleted successfully"},
                status=status.HTTP_200_OK,
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)


############ """""""" ADMIN """"""""""#########


"""""" """ TOUR GUIDE  """ """""" """""" """"""


class GetAllTourLocationsViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_rooms = Tour_locations.objects.all()
            room_data_dic = serializers.TourlocationsSerializer(sm_rooms, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(room_data_dic.data)):
            created_user = room_data_dic.data[i].get("user")
            try:
                package_inst = User_Register.objects.get(id=created_user)

                room_data_dic.data[i].update(
                    {
                        "user": {
                            "id": package_inst.id,
                            "name": package_inst.name,
                            "mobile": package_inst.mobile,
                        }
                    }
                )
            except:
                room_data_dic.data[i].update(
                    {
                        "user": {
                            "id": created_user,
                            "message": "Deleted user",
                        }
                    }
                )

        return Response(room_data_dic.data, status=status.HTTP_200_OK)


class GetAllTourPackagesViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_rooms = Tour_Packages.objects.all()
            room_data_dic = serializers.TourPackagesSerializer(sm_rooms, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(room_data_dic.data)):
            created_user = room_data_dic.data[i].get("user")
            try:
                package_inst = User_Register.objects.get(id=created_user)

                room_data_dic.data[i].update(
                    {
                        "user": {
                            "id": package_inst.id,
                            "name": package_inst.name,
                            "mobile": package_inst.mobile,
                        }
                    }
                )
            except:
                room_data_dic.data[i].update(
                    {
                        "user": {
                            "id": created_user,
                            "message": "Deleted user",
                        }
                    }
                )
        return Response(room_data_dic.data, status=status.HTTP_200_OK)


class GetAllTourGuiderViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_rooms = TourGuide_Reg.objects.all()
            tourguide_data_dic = serializers.TourGuideRegSerializer(sm_rooms, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(tourguide_data_dic.data)):
            created_user = tourguide_data_dic.data[i].get("user")
            try:
                package_inst = User_Register.objects.get(id=created_user)

                tourguide_data_dic.data[i].update(
                    {
                        "user": {
                            "id": package_inst.id,
                            "name": package_inst.name,
                            "mobile": package_inst.mobile,
                        }
                    }
                )
            except:
                tourguide_data_dic.data[i].update(
                    {
                        "user": {
                            "id": created_user,
                            "message": "Deleted user",
                        }
                    }
                )
            created_tour_locations = tourguide_data_dic.data[i].get("tour_locations")
            try:
                package_inst = Tour_locations.objects.get(id=created_tour_locations)

                tourguide_data_dic.data[i].update(
                    {
                        "tour_locations": {
                            "id": package_inst.id,
                            "locations": package_inst.locations,
                            "status": package_inst.status,
                        }
                    }
                )
            except:
                tourguide_data_dic.data[i].update(
                    {
                        "tour_locations": {
                            "id": created_tour_locations,
                            "message": "Deleted tour_locations",
                        }
                    }
                )
            created_packages = tourguide_data_dic.data[i].get("packages")
            try:
                package_inst = Tour_Packages.objects.get(id=created_packages)

                tourguide_data_dic.data[i].update(
                    {
                        "packages": {
                            "id": package_inst.id,
                            "location_ids": package_inst.location_ids,
                            "package_amount": package_inst.package_amount,
                        }
                    }
                )
            except:
                tourguide_data_dic.data[i].update(
                    {
                        "packages": {
                            "id": created_packages,
                            "message": "Deleted Packages",
                        }
                    }
                )

        return Response(tourguide_data_dic.data, status=status.HTTP_200_OK)


class GetClientslAllViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_users = User_Register.objects.all()
            users_data_dic = serializers.UserRegisterSerializer(sm_users, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)


class GetHotelAllViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_users = Reg_Hotel.objects.all()
            users_data_dic = serializers.HotelRegisterSerializer(sm_users, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)


class GetRoomALLViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_rooms = Room_Register.objects.all()
            room_data_dic = serializers.RoomRegisterSerializer(sm_rooms, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(room_data_dic.data)):
            created_hotel_id = room_data_dic.data[i].get("hotel_id")
            try:
                hotel_inst = Reg_Hotel.objects.get(id=created_hotel_id)

                room_data_dic.data[i].update(
                    {
                        "hotel_id": {
                            "id": hotel_inst.id,
                            "hotel_name": hotel_inst.hotel_name,
                            "hotel_city": hotel_inst.hotel_city,
                            "room_rates": hotel_inst.room_rates,
                        }
                    }
                )
            except:
                room_data_dic.data[i].update(
                    {"hotel_id": {"id": created_hotel_id, "message": "No Hotel found"}}
                )

        return Response(room_data_dic.data, status=status.HTTP_200_OK)


class GetCabAllViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_cabs = Cabs_Reg.objects.all()
            cabs_data_dic = serializers.CabRegisterSerializer(sm_cabs, many=True)
        except:
            return Response(
                {"message": "Sorry No cab found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(cabs_data_dic.data, status=status.HTTP_200_OK)


class GetDriverAllViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_driver = Driver_Reg.objects.all()
            driver_data_dic = serializers.DriverRegisterSerializer(sm_driver, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(driver_data_dic.data)):
            created_user_id = driver_data_dic.data[i].get("user")
            try:
                user_inst = User_Register.objects.get(id=created_user_id)

                driver_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                driver_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )

        return Response(driver_data_dic.data, status=status.HTTP_200_OK)
