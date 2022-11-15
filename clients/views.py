from django.shortcuts import render
import requests

# Create your views here.
from rest_framework import serializers, viewsets
from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail
import random
import string

import jwt
import datetime
from json import JSONEncoder
from uuid import UUID

from uritemplate import partial

from users.models import User_Guide_Booking

from . import serializers

# Create your views here.
"""Model Package """
from .models import (
    HotelImages,
    Reg_Hotel,
    RoomImages,
    Tour_Packages,
    Tour_locations,
    TourGuide_Reg,
    User_Register,
    Room_Register,
    Driver_Reg,
    Cabs_Reg,
    Client_login,
    UserOTP,
)

from shangkai_app.models import (
    Hotel_Category,
)


old_default = JSONEncoder.default


def new_default(self, obj):
    if isinstance(obj, UUID):
        return str(obj)
    return old_default(self, obj)


JSONEncoder.default = new_default


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

        user_id = random.randint(111111, 999999)
        user_ip = request.POST.get("user_ip", None)
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        mobile = request.POST.get("mobile", None)
        password = request.POST.get("password", None)
        image = request.POST.get("image", None)
        role = request.POST.get("user_role", None)
        otp = random.randint(1111, 9999)
        token = "".join(random.choices(string.ascii_uppercase + string.digits, k=80))

        if email is not None:
            user_already_email_exists = User_Register.objects.filter(
                email=email
            ).exists()
            if user_already_email_exists:
                return Response(
                    {"message": "Email Already Exists !"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        users_inst = User_Register.objects.create(
            user_id=user_id,
            user_ip=user_ip,
            name=name,
            email=email,
            mobile=mobile,
            password=password,
            user_type=role,
            otp=otp,
            image=image,
        )
        users_inst.save()

        subject = "Team Shangkai : Account verification"
        message = f"Hello, {users_inst.name}, Account verification mail sent to your email : https://shangkai.in/verify/clients.php?email={email}&token={token}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            users_inst.email,
        ]
        send_mail(subject, message, email_from, recipient_list)

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
                {"message": "Your Password has been changed Successfully "},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ClientVerifyEmailViewSet(viewsets.ViewSet):
    def create(self, request):

        email = request.POST.get("email", None)
        token = "".join(random.choices(string.ascii_uppercase + string.digits, k=80))

        if email is None:

            return Response(
                {"message": "Enter email id !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            users_inst = User_Register.objects.filter(email=email)
            users_data_dic = serializers.UserRegisterSerializer(users_inst, many=True)

            subject = "Team Shangkai : Account verification"
            message = f"Hello, Please find below the link to change your password : https://shangkai.in/verify/clients_account.php?email={email}&token={token}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [
                email,
            ]
            send_mail(subject, message, email_from, recipient_list)

        except:
            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)


class ClientloginViewSet(viewsets.ViewSet):

    def create(self, request):

        email = request.POST.get("email", None)
        password = request.POST.get("password", None)

        user_inst = User_Register.objects.filter(email=email, password=password).first()

        if user_inst is None:
            return Response(
                {"message": "Invalid Username or password !"}, status=status.HTTP_400_BAD_REQUEST
            )
        
        otp=""
        for i in range(6):
            otp+=str(random.randint(1,9))
        res = requests.get(f"https://2factor.in/API/V1/6b9b1b0e-8b1f-11eb-8089-0200cd936042/SMS/{user_inst.mobile}/{otp}/SHANGKAI")
        if(res.status_code == 200 and res.json()["Status"] == "Success"):
            session_id = res.json()["Details"]
            UserOTP.objects.create(session_id=session_id,used_for="login",otp=otp,mobile=user_inst.mobile)
            return Response(
                {"message": "OTP has been sent to your mobile number !"}, status=status.HTTP_200_OK
            )
        return Response(
            {"message": "Some error occured"}, status=status.HTTP_400_BAD_REQUEST
        )

class ClientOTPViewSet(viewsets.ViewSet):

    def create(self, request):

        otp = request.POST.get("otp", None)
        mobile = request.POST.get("mobile", None)
        email = request.POST.get("email", None)

        user_inst = UserOTP.objects.filter(mobile=mobile,otp=otp,used_for="login").first()

        if user_inst is None:
            return Response(
                {"message": "Invalid OTP !"}, status=status.HTTP_400_BAD_REQUEST
        )
        res = requests.get(f"https://2factor.in/API/V1/6b9b1b0e-8b1f-11eb-8089-0200cd936042/SMS/VERIFY/{user_inst.session_id}/{otp}")
        if(res.status_code == 200 and res.json()["Status"] == "Success"):
            user_inst.delete()
            user_inst = User_Register.objects.filter(email=email).first()
            access_payload = {
                "id": user_inst.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=14),
                "iat": datetime.datetime.utcnow(),
            }
            access_token = jwt.encode(
                access_payload, settings.SECRET_KEY, algorithm="HS256"
            )

            refresh_payload = {
                "user": user_inst.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=14),
                "iat": datetime.datetime.utcnow(),
            }
            refresh_token = jwt.encode(
                refresh_payload, settings.REFRESH_TOKEN_SECRET, algorithm="HS256"
            )

            return Response(
                {"access_token": access_token, "refresh_token": refresh_token},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "Invalid OTP !"}, status=status.HTTP_400_BAD_REQUEST
        )

class HotelRegistrationViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_users = Reg_Hotel.objects.filter(user=user_id)
            users_data_dic = serializers.HotelViewSerializer(sm_users, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.HotelRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Hotel Registered Successfully !"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = Reg_Hotel.objects.filter(id=pk,user=user_id).first()
            serializer = serializers.HotelRegisterSerializer(post_inst, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
            scm_post_inst = Reg_Hotel.objects.filter(id=pk,user=user_id).first()
            scm_post_inst.delete()
            return Response(
                {"message": "Hotel Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_400_BAD_REQUEST)


class RoomRegistrationViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        # hotel_id = request.POST.get("hotel_id", None)

        try:
            sm_users = Room_Register.objects.filter(user=user_id)
            users_data_dic = serializers.RoomViewSerializer(sm_users, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.RoomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Room Registered Successfully !"},
                status=status.HTTP_201_CREATED,
            )
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        if user_id is None:
            return Response(
                {"message": "Please provide a user_id"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = Room_Register.objects.filter(id=pk, user=user_id).first()
            serializer = serializers.RoomRegisterSerializer(post_inst, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                {"message": "Something went to wrong ! Try again !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_post_inst = Room_Register.objects.filter(id=pk, user=user_id).first()
            scm_post_inst.delete()
            return Response(
                {"message": "Room Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)

class HotelImagesViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = serializers.HotelImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)
        hotel_id = request.GET.get("hotel_id", None)
        try:
            scm_post_inst = HotelImages.objects.filter(id=pk, user=user_id, hotel_id=hotel_id).first()
            scm_post_inst.delete()
            return Response(
                {"message": "Hotel Images Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT
            )
        except:
            return Response({"message": "Please provide correct user, hotel and hotelimage id"}, status=status.HTTP_400_BAD_REQUEST)
        
class RoomImagesViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = serializers.RoomImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)
        room_id = request.GET.get("room_id", None)
        try:
            scm_post_inst = RoomImages.objects.filter(id=pk, user=user_id, room_id=room_id).first()
            scm_post_inst.delete()
            return Response(
                {"message": "Room Images Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT
            )
        except:
            return Response({"message": "Please provide correct user, room and roomimage id"}, status=status.HTTP_400_BAD_REQUEST)

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
        serializer = serializers.DriverRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        if user_id is None:
            return Response(
                {"message": "Please provide a user_id"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = Driver_Reg.objects.filter(id=pk, user=user_id).first()
            serializer = serializers.DriverRegisterSerializer(post_inst, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
            scm_post_inst = Driver_Reg.objects.filter(id=pk, user=user_id).first()
            scm_post_inst.delete()
            return Response(
                {"message": "Driver Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_400_BAD_REQUEST)


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
        serializer = serializers.CabRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        if user_id is None:
            return Response(
                {"message": "Please provide a user_id"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = Cabs_Reg.objects.filter(id=pk, user=user_id).first()
            serializer = serializers.CabRegisterSerializer(post_inst, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
                {"message": "Cab Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_400_BAD_REQUEST)


########### STATUS UPDATE ######################

### HOTEL
class HotelUpdateStatusViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_users = Reg_Hotel.objects.filter(user=user_id)
            users_data_dic = serializers.HotelRegisterSerializer(sm_users, many=True)
        except:
            return Response({"message": "Sorry No data found !"})
        return Response(users_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        sttus = request.POST.get("status", None)

        if user_id is None:
            return Response({"message": "Invalid Request"})

        try:
            post_inst = Reg_Hotel.objects.filter(user=user_id,id=pk).first()
            post_inst.status = sttus

            # post_inst.is_edited = True
            post_inst.save()

            return Response({"message": "Hotel Status Updated Sucessfully","data":serializers.HotelRegisterSerializer(post_inst).data},status=status.HTTP_200_OK)

        except:
            return Response({"message": "Something went to wrong ! Try again !"}, status=status.HTTP_400_BAD_REQUEST,)


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
        sttus = request.POST.get("status", None)

        if user_id is None:
            return Response({"message": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            post_inst = Room_Register.objects.filter(id=pk, user=user_id).first()
            post_inst.states = sttus
            post_inst.save()

            return Response({"message": "Room Status Updated Sucessfully","data":serializers.RoomRegisterSerializer(post_inst).data},status=status.HTTP_200_OK)

        except:
            return Response({"message": "Something went to wrong ! Try again !"}, status=status.HTTP_400_BAD_REQUEST,)


###### CABS
class CabUpdateStatusViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_cabs = Cabs_Reg.objects.filter(user=user_id)
            cabs_data_dic = serializers.CabRegisterSerializer(sm_cabs, many=True)
        except:
            return Response({"message": "Sorry No data found !"})

        return Response(cabs_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        status = request.POST.get("status", None)

        if user_id is None:
            return Response({"message": "Invalid Request"})

        try:
            post_inst = Cabs_Reg.objects.get(id=pk)
            post_inst.status = status

            post_inst.is_edited = True
            post_inst.save()

            return Response({"message": "Cab Status Updated Sucessfully"})

        except:
            return Response({"message": "Something went to wrong ! Try again !"})


##### DRIVERS
class DriverUpdateStatusViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_driver = Driver_Reg.objects.filter(user=user_id)
            driver_data_dic = serializers.DriverRegisterSerializer(sm_driver, many=True)
        except:
            return Response({"message": "Sorry No data found !"})

        return Response(driver_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        status = request.POST.get("status", None)

        if user_id is None:
            return Response({"message": "Invalid Request"})

        try:
            post_inst = Driver_Reg.objects.get(id=pk)
            post_inst.status = status
            post_inst.is_edited = True
            post_inst.save()

            return Response({"message": "Driver Status Updated Sucessfully"})

        except:
            return Response({"message": "Something went to wrong ! Try again !"})


###### TOUR LOCATIONS
class TourLocationsUpdateStatusViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_rooms = Tour_locations.objects.filter(user=user_id)
            room_data_dic = serializers.TourlocationsSerializer(sm_rooms, many=True)
        except:
            return Response({"message": "Sorry No data found !"})

        return Response(room_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        status = request.POST.get("status", None)

        if user_id is None:
            return Response({"message": "Invalid Request"})

        try:
            post_inst = Tour_locations.objects.get(id=pk)
            post_inst.status = status
            post_inst.is_edited = True
            post_inst.save()

            return Response({"message": "Tour Location Status Updated Sucessfully"})

        except:
            return Response({"message": "Something went to wrong ! Try again !"})


###### TOUR PACKAGES
class TourPackagesUpdateStatusViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_rooms = Tour_Packages.objects.filter(user=user_id)
            room_data_dic = serializers.TourPackagesSerializer(sm_rooms, many=True)
        except:
            return Response({"message": "Sorry No data found !"})
        return Response(room_data_dic.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        status = request.POST.get("status", None)

        if user_id is None:
            return Response({"message": "Invalid Request"})

        try:
            post_inst = Tour_Packages.objects.get(id=pk)
            post_inst.status = status
            post_inst.is_edited = True
            post_inst.save()

            return Response({"message": "Tour Package Status Updated Sucessfully"})

        except:
            return Response({"message": "Something went to wrong ! Try again !"})


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
            return Response({"message": "Invalid Request"})

        try:
            post_inst = TourGuide_Reg.objects.get(id=pk)
            post_inst.status = status
            post_inst.is_edited = True
            post_inst.save()

            return Response({"message": "Tour Guider Status Updated Sucessfully"})

        except:
            return Response({"message": "Something went to wrong ! Try again !"})


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
        serializer = serializers.TourPackagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk=None):
        try:
            item = Tour_Packages.objects.get(id=pk)
        except:
            return Response(
                "Sorry No data found !", status=status.HTTP_400_BAD_REQUEST
            )
        serializer = serializers.TourPackagesSerializer(item,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
            client = User_Register.objects.get(id=user_id)
            sm_rooms = TourGuide_Reg.objects.filter(user=client)
            tourguide_data_dic = serializers.TourGuideRegViewSerializer(sm_rooms, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(tourguide_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.TourGuideRegSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update(self,request,pk=None):
        user_id = request.GET.get("user_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_tourguide_inst = TourGuide_Reg.objects.filter(id=pk,user=user_id).first()
            tour_guide_serializer = serializers.TourGuideRegSerializer(scm_tourguide_inst, data=request.data,partial=True)
            if tour_guide_serializer.is_valid():
                tour_guide_serializer.save()
                return Response(
                    tour_guide_serializer.data,
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)
    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_tourguide_inst = TourGuide_Reg.objects.filter(id=pk,user=user_id).first()
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
        date = request.GET.get("date", None)
        try:
            sm_rooms = TourGuide_Reg.objects.all()
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        qs = User_Guide_Booking.objects.filter(booking_date=date)
        l = []
        data = []
        for i in qs:
            l.append(str(i.id))
        for item in sm_rooms:
            if str(item.id) in l:
                continue
            else:
                d = serializers.TourGuideRegViewSerializer(item).data
                data.append(d)
        return Response(data, status=status.HTTP_200_OK)


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
