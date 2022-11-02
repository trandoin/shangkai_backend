from datetime import timedelta
import datetime
import uuid
from django.shortcuts import render
import requests
from rest_framework import serializers, viewsets
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status

from shangkai_app.helpers import html_to_pdf
from users.helpers import check_rooms_availaible, send_hotel_book_email
from . import serializers
import random
import string
import smtplib
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail
from shangkai_app.razorpay import client, verify_payment
import os
from dotenv import load_dotenv
load_dotenv()


"""Model Package """
from .models import (
    User_Account_Details,
    User_Cab_Booking,
    User_Guide_Booking,
    User_Hotel_Booking,
    Normal_UserReg,
    User_Hotel_Cart,
    User_Cab_Cart,
    User_Hotel_Order,
    User_Hotel_Payment,
    User_Hotspots_Bookings,
    User_Hotspots_Cart,
    User_Trip_Cart,
    User_Cab_Payment,
    User_Trip_Booking,
    User_Trip_Order,
    User_Trips_Payment,
    User_Ratings,
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
    Coupon,
    Hot_Spots,
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

        user_id = random.randint(111111, 999999)
        user_ip = request.POST.get("user_ip", None)
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        mobile = request.POST.get("mobile", None)
        otp = random.randint(1111, 9999)
        password = request.POST.get("password", None)
        image = request.POST.get("image", None)
        token = "".join(random.choices(string.ascii_uppercase + string.digits, k=80))
        
        if email is not None:
            user_already_email_exists = Normal_UserReg.objects.filter(
                email=email
            ).exists()
            if user_already_email_exists:
                return Response(
                    {"message": "Email Already Exists !"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        users_inst = Normal_UserReg.objects.create(
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
        # mail_context = {
        #     "content_message": f"Your OTP verification code is {otp}",
        # }
        # html_message = render_to_string("email/user_email_verify.html", mail_context)
        # send_mail(
        #     "Reading Right : OTP verification",
        #     "Your OTP verification code is {otp}".format(otp=otp),
        #     "businessinfotrando@gmail.com",
        #     [users_inst.email],
        #     fail_silently=False,
        #     html_message=html_message,
        # )
        subject = "Team Shangkai : Account verification"
        message = f"Hello, {users_inst.name}, Account verification mail sent to your email : https://shangkai.in/verify/?email={email}&token={token}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            users_inst.email,
        ]
        send_mail(subject, message, email_from, recipient_list)

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


# user_account.php
class UserVerifyEmailViewSet(viewsets.ViewSet):
    def create(self, request):

        email = request.POST.get("email", None)
        token = "".join(random.choices(string.ascii_uppercase + string.digits, k=80))

        if email is None:

            return Response(
                {"message": "Enter email id !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            users_inst = Normal_UserReg.objects.filter(email=email)
            users_data_dic = serializers.NormalUserRegisterSerializer(
                users_inst, many=True
            )

            subject = "Team Shangkai : Account verification"
            message = f"Hello, Please find below the link to change your password : https://shangkai.in/verify/user_account.php?email={email}&token={token}"
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


class UserUpdatePasswordViewSet(viewsets.ViewSet):
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

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        password = request.POST.get("password", None)

        if user_id is None:
            return Response(
                {"message": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user_inst = Normal_UserReg.objects.get(id=pk)
            user_inst.password = password
            user_inst.is_edited = True
            user_inst.save()

            return Response(
                {"message": "Your Password has been changed Successfully "},
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


class UserRationsViewSet(viewsets.ViewSet):
    def list(self, request):
        item_id = request.GET.get("item_id", None)
        item_type = request.GET.get("item_type", None)
        try:
            sm_user = User_Ratings.objects.filter(item_id=item_id, item_type=item_type)
            user_data_dic = serializers.UserRatingsSerializer(sm_user, many=True)
        except:
            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for i in range(0, len(user_data_dic.data)):
            created_user_id = user_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                user_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                user_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted user"}}
                )

        return Response(user_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        cleaness = request.POST.get("cleaness", None)
        hospitility = request.POST.get("hospitility", None)
        location = request.POST.get("location", None)
        aesthetic = request.POST.get("aesthetic", None)
        value = request.POST.get("value", None)
        scenic_beauty = request.POST.get("scenic_beauty", None)
        surrounding = request.POST.get("surrounding", None)
        safety_security = request.POST.get("safety_security", None)
        item_id = request.POST.get("item_id", None)
        item_type = request.POST.get("item_type", None)
        message = request.POST.get("message", None)

        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
        except:

            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = User_Ratings.objects.create(
            user_id=user_id,
            cleaness=cleaness,
            hospitility=hospitility,
            location=location,
            aesthetic=aesthetic,
            value=value,
            scenic_beauty=scenic_beauty,
            surrounding=surrounding,
            safety_security=safety_security,
            item_id=item_id,
            item_type=item_type,
            message=message,
        )
        users_inst.save()

        users_data = serializers.UserRatingsSerializer(
            User_Ratings.objects.filter(id=users_inst.id), many=True
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
        check_in_time = request.POST.get("check_in_time", None)
        check_out_date = request.POST.get("check_out_date", None)
        check_out_time = request.POST.get("check_out_time", None)
        guest_no = request.POST.get("guest_no", None)
        rooms = request.POST.get("rooms", None)
        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            hotel_inst = Reg_Hotel.objects.get(id=hotel_id)
            room_inst = Room_Register.objects.get(id=room_id)
        except:

            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        check_in_date = datetime.datetime.strptime(check_in_date, "%Y-%m-%d").date()
        check_out_date = datetime.datetime.strptime(check_out_date, "%Y-%m-%d").date()
        check_in_time = datetime.datetime.strptime(check_in_time, "%H:%M:%S").time()
        check_out_time = datetime.datetime.strptime(check_out_time, "%H:%M:%S").time()
        no_day = (check_out_date - check_in_date).days
        amount_booking = int(rooms) * int(room_inst.room_rates) * int(no_day)
        hotel_cart_inst = User_Hotel_Cart.objects.create(
            user=user_inst,
            hotel_id=hotel_inst,
            room_id=room_inst,
            check_in_date=check_in_date,
            check_in_time=check_in_time,
            check_out_date=check_out_date,
            check_out_time=check_out_time,
            guest_no=guest_no,
            rooms=rooms,
            amount_booking=amount_booking,
        )
        hotel_cart_data = serializers.HotelCartSerializer(
            hotel_cart_inst
        )
        return Response(hotel_cart_data.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        cart_status = request.POST.get("cart_status", None)

        if pk is None and user_id is None:
            return Response(
                {"message": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = User_Hotel_Cart.objects.filter(id=pk, user=user_id).first()
            post_inst.booking_status = cart_status
            post_inst.save()

            return Response(
                {"message": "Hotel Cart Updated Sucessfully","data": serializers.HotelCartSerializer(post_inst).data},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Sorry No data found with this cart id"},
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
            scm_post_inst = User_Hotel_Cart.objects.filter(id=pk,user=user_id).first()
            scm_post_inst.delete()
            return Response(
                {"message": "Successfully Cart Removed"}, status=status.HTTP_204_NO_CONTENT
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_400_BAD_REQUEST)
        
class HotelOrderViewSet(viewsets.ViewSet):
    def create(self, request):
        user_id = request.POST.get("user_id", None)
        hotel_cart = request.POST.get("hotel_cart", None)
        currency = request.POST.get('currency', 'INR')
        coupon_code = request.POST.get('coupon_code',None)
        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            hotel_cart_inst = User_Hotel_Cart.objects.get(id=hotel_cart)
        except:
            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # first check if room is availaible
        cin = hotel_cart_inst.check_in_date
        cout = hotel_cart_inst.check_out_date
        hotel_inst = hotel_cart_inst.hotel_id
        room_inst = hotel_cart_inst.room_id
        no_rooms , sttus = check_rooms_availaible(cin,cout,hotel_inst,room_inst,hotel_cart_inst.rooms)
        if not sttus:
            return Response(
                {"message": f"Only {no_rooms} rooms available !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # then create an order for payment
        amount = int(hotel_cart_inst.amount_booking)
        receipt = str(uuid.uuid4())
        coupon_applied = False
        if coupon_code:
            try:
                Coupon_inst = Coupon.objects.get(id=coupon_code)
                amount = amount - (Coupon_inst.discount * amount) / 100
                coupon_applied = True
            except:
                pass
        data = dict(amount=int(amount * 100), currency=currency, receipt=receipt)
        try:
            order = client.order.create(data=data)
            User_Hotel_Order.objects.create(
                id = order['id'],
                currency = currency,
                amount = str(amount * 100),
                cart_item = hotel_cart_inst
                )
            return Response({"order":order,"coupon_applied":coupon_applied}, status=200)
        except Exception as e:
            print(e)
            return Response('error', status=500)

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
        user_ip = request.POST.get("user_ip", None)
        payment_id = request.POST.get("payment_id", "")
        order_id = request.POST.get("order_id", "")
        signature = request.POST.get("signature", "")
        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            hotel_order_inst = User_Hotel_Order.objects.get(id=order_id)
            hotel_cart_inst = hotel_order_inst.cart_item
            hotel_inst = hotel_cart_inst.hotel_id
            room_inst = hotel_cart_inst.room_id
        except:
            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        no_rooms,sttus = check_rooms_availaible(hotel_cart_inst.check_in_date,hotel_cart_inst.check_out_date,hotel_inst,room_inst,hotel_cart_inst.rooms)
        if not sttus:
            return Response(
                {"message": f"Only {no_rooms} rooms available !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if verify_payment(payment_id, order_id, signature):
        # if  True:
            users_inst = User_Hotel_Booking.objects.create(
                user=user_inst,
                user_ip=user_ip,
                hotel_id=hotel_inst,
                room_id=room_inst,
                hotel_bookid=order_id,
                check_in_date=hotel_cart_inst.check_in_date,
                check_in_time=hotel_cart_inst.check_in_time,
                check_out_date=hotel_cart_inst.check_out_date,
                check_out_time=hotel_cart_inst.check_out_time,
                guest_no=int(hotel_cart_inst.guest_no),
                rooms=int(hotel_cart_inst.rooms),
                amount_booking=hotel_order_inst.amount,
                payment_id=payment_id,
                order_id=order_id,
                signature=signature,
            )
            hotel_cart_inst.delete()
            #  send sms and email
            send_hotel_book_email(
                name=user_inst.name,
                booking_id=users_inst.hotel_bookid,
                hotel=hotel_inst.hotel_name,
                room=room_inst.room_type,
                check_in_date=hotel_cart_inst.check_in_date.strftime("%d %b %Y, %I:%M %p"),
                check_out_date=hotel_cart_inst.check_out_date.strftime("%d %b %Y, %I:%M %p"),
                rooms=str(hotel_cart_inst.rooms),
                amount=str(hotel_order_inst.amount)[:-2],
                to=user_inst.email,
            )
            #   send sms to user as a transactional message
            res = requests.post(
                f"http://2factor.in/API/V1/${os.getenv('TWO_FACTOR_KEY')}/ADDON_SERVICES/SEND/TSMS",
                data = {
                    "From": "SNGKAI",
                    "To": user_inst.mobile,
                    "TemplateName": "hotel_booking",
                    "VAR1": user_inst.name,
                    "VAR2": f"{hotel_inst.hotel_name} - {room_inst.room_type}",
                    "VAR3": order_id,
                    "VAR4": hotel_cart_inst.check_in_date.strftime("%d %b %Y, %I:%M %p"),
                    "VAR5": hotel_cart_inst.check_out_date.strftime("%d %b %Y, %I:%M %p"),
                    "VAR6": str(hotel_cart_inst.rooms),
                    "VAR7": str(hotel_order_inst.amount)[:-2],
                    "VAR8": user_inst.mobile,
                }
            )
            print(res.text)
            return Response(
                "serializers.HotelBookingSerializer(users_inst).data",
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"message": "Invalid data !"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        razorpay_id = request.POST.get("razorpay_id", None)
        sttus = request.POST.get("status", None)

        if pk is None and user_id is None:
            return Response({"message": "Invalid Input"})

        try:
            post_inst = User_Hotel_Booking.objects.get(id=pk)
            post_inst.razorpay_id = razorpay_id
            post_inst.booking_status = sttus
            post_inst.save()

            return Response({"message": "Hotel has been booked Sucessfully"})

        except:
            return Response({"message": "Invalid request"})

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)

        if user_id is None and pk is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_post_inst = User_Hotel_Booking.objects.filter(id=pk,user=user_id).first()
            scm_post_inst.delete()
            return Response(
                {"message": "Hotel Booking Removed Successfully"},
                status=status.HTTP_204_NO_CONTENT,
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
        user_ip = request.POST.get("user_ip", None)
        cart_item_id = request.POST.get("cart_item_id", None)
        payment_id = request.POST.get("payment_id", None)
        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            cart_item_inst = User_Hotel_Cart.objects.filter(id=cart_item_id,user=user_id).first()
            hotel_inst = cart_item_inst.hotel_id
            room_inst = cart_item_inst.room_id
        except:

            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        users_inst = serializers.HotelBookingSerializer(
            data={            
            "user":user_id,
            "user_ip":user_ip,
            "hotel_id":cart_item_inst.hotel_id.id,
            "room_id":cart_item_inst.room_id.id,
            "hotel_bookid":"123456",
            "check_in_date":cart_item_inst.check_in_date,
            "check_in_time":cart_item_inst.check_in_time,
            "check_out_date":cart_item_inst.check_out_date,
            "check_out_time":cart_item_inst.check_out_time,
            "guest_no":cart_item_inst.guest_no,
            "rooms":cart_item_inst.rooms,
            "amount_booking":cart_item_inst.amount_booking,
        })
        if users_inst.is_valid(raise_exception=True):
            new_booking = users_inst.save()
            cin = new_booking.check_in_date
            cout = new_booking.check_out_date
            new_booking.delete()
            # check if room is available or not
            hotel_booking = User_Hotel_Booking.objects.filter(
                hotel_id=hotel_inst,
                room_id=room_inst,
                check_in_date__gte=cin,
                check_in_date__lte=cout,
            )
            hotel_booking2 = User_Hotel_Booking.objects.filter(
                hotel_id=hotel_inst,
                room_id=room_inst,
                check_out_date__gte=cin,
                check_out_date__lte=cout,
            )
            hotel_booking3 = User_Hotel_Booking.objects.filter(
                hotel_id=hotel_inst,
                room_id=room_inst,
                check_in_date__lte=cin,
                check_out_date__gte=cout,
            )
            hotel_booking4 = User_Hotel_Booking.objects.filter(
                hotel_id=hotel_inst,
                room_id=room_inst,
                check_in_date__gte=cin,
                check_out_date__lte=cout,
            )
            hotel_booking = hotel_booking.union(hotel_booking2)
            hotel_booking = hotel_booking.union(hotel_booking3)
            hotel_booking = hotel_booking.union(hotel_booking4)            
            if len(hotel_booking) > 0:
                day_count = (cout - cin).days + 1
                for single_date in (cin + timedelta(n) for n in range(day_count)):
                    count=0
                    for i in range(0, len(hotel_booking)):
                        if single_date >= hotel_booking[i].check_in_date and single_date <= hotel_booking[i].check_out_date:
                            count+=hotel_booking[i].rooms
                    if int(room_inst.no_rooms) < int(count) + int(cart_item_inst.rooms):
                        return Response(
                            {"message": f"Only {int(room_inst.no_rooms) - int(count)} rooms available !"},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
            """
            accept payment by razorpay
            """
            payment_status = True
            transaction_id  = "sfgsd"
            if payment_status:
                new_booking = users_inst.save()
                new_booking.razorpay_id = transaction_id
                new_booking.save()
                cart_item_inst.delete()
                users_inst = User_Hotel_Payment.objects.create(
                    user=user_inst,
                    hotel_booking=new_booking,
                    payment_id=transaction_id,
                )
                users_inst.save()

                users_data = serializers.UserHotelPaymentSerializer(
                    User_Hotel_Payment.objects.filter(id=users_inst.id), many=True
                )
                #   send sms to user as a transactional message
                # res = requests.post(
                #     f"http://2factor.in/API/V1/293832-67745-11e5-88de-5600000c6b13/ADDON_SERVICES/SEND/TSMS",
                #     data = {
                #         "From": "Hotel",
                #         "To": user_inst.mobile,
                #         "TemplateName": "HotelBooking",
                #         "VAR1": hotel_inst.hotel_name,
                #         "VAR2": hotel_inst.hotel_address,
                #         "VAR3": hotel_inst.hotel_city,
                #         "VAR4": hotel_inst.hotel_state,
                #         "VAR5": hotel_inst.hotel_country,
                #         "VAR6": hotel_inst.hotel_pincode,
                #     }
                # )
                return Response(
                    {
                        "booking":serializers.HotelBookingSerializer(new_booking).data,
                        "payment":users_data.data,
                        },
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                {"message": "Sorry payment failed !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {"message": "Invalid data !"},
            status=status.HTTP_400_BAD_REQUEST,
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

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        cart_id = request.POST.get("cart_id", None)
        cart_status = request.POST.get("cart_status", None)

        if pk is None and user_id is None:
            return Response(
                {"message": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = User_Cab_Cart.objects.get(id=pk)
            post_inst.booking_status = cart_status
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Cab Cart Updated Sucessfully"},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Sorry No data found with this cart id"},
                status=status.HTTP_400_BAD_REQUEST,
            )

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

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        razorpay_id = request.POST.get("razorpay_id", None)
        status = request.POST.get("status", None)

        if pk is None and user_id is None:
            return Response({"message": "Invalid Input"})

        try:
            post_inst = User_Cab_Booking.objects.get(id=pk)
            post_inst.razorpay_id = razorpay_id
            post_inst.booking_status = status
            post_inst.is_edited = True
            post_inst.save()

            return Response({"message": "Cab has been booked Sucessfully"})

        except:
            return Response({"message": "Invalid request"})

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

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_post_inst = User_Trip_Cart.objects.filter(id=pk,user_id=user_id).first()
            scm_post_inst.delete()
            return Response(
                {"message": "Successfully Cart Removed"}, status=status.HTTP_200_OK
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        trip_cart_status = request.POST.get("cart_status", None)

        if pk is None and user_id is None:
            return Response(
                {"message": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = User_Trip_Cart.objects.filter(id=pk,user_id=user_id).first()
            post_inst.trip_cart_status = trip_cart_status
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

class UserTripsOrderViewset(viewsets.ViewSet):
    def create(self, request):
        user_id = request.POST.get("user_id", None)
        trip_cart = request.POST.get("trip_cart", None)
        currency = request.POST.get('currency', 'INR')
        coupon_code = request.POST.get('coupon_code',None)
        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            trip_cart_inst = User_Trip_Cart.objects.get(id=trip_cart)
        except:
            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        amount = int(trip_cart_inst.no_guests) * int(trip_cart_inst.trip_id.price)
        receipt = str(uuid.uuid4())
        coupon_applied = False
        if coupon_code:
            try:
                Coupon_inst = Coupon.objects.get(id=coupon_code)
                amount = amount - (Coupon_inst.discount * amount) / 100
                coupon_applied = True
            except:
                pass
        data = dict(amount=int(amount * 100), currency=currency, receipt=receipt)
        try:
            order = client.order.create(data=data)
            User_Trip_Order.objects.create(
                id = order['id'],
                currency = currency,
                amount = str(amount * 100),
                cart_item = trip_cart_inst
                )
            return Response({"order":order,"coupon_applied":coupon_applied}, status=200)
        except Exception as e:
            print(e)
            return Response('error', status=500)

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
        payment_id = request.POST.get("payment_id", "")
        order_id = request.POST.get("order_id", "")
        signature = request.POST.get("signature", "")

        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            trip_order_inst = User_Trip_Order.objects.get(id=order_id)
            trip_cart_inst = User_Trip_Cart.objects.get(id=trip_order_inst.cart_item.id)
            trip_inst = My_Trips.objects.get(id=trip_cart_inst.trip_id.id)
        except:
            return Response(
                {"message": "Invalid Request!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if verify_payment(payment_id, order_id, signature):
            users_inst = User_Trip_Booking.objects.create(
                user=user_inst,
                trip_id=trip_inst,
                no_guests=trip_cart_inst.no_guests,
                trip_ammount=trip_order_inst.amount,
                payment_id=payment_id,
                order_id=order_id,
                signature=signature,
            )
            users_data = serializers.UserTripBookingSerializer(
                users_inst
            )
            trip_cart_inst.delete()
            #  send sms and email
            return Response(users_data.data, status=status.HTTP_200_OK)
        return Response("not a valid payment", status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        razorpay_id = request.POST.get("razorpay_id", None)
        status = request.POST.get("status", None)

        if pk is None and user_id is None:
            return Response({"message": "Invalid Input"})

        try:
            post_inst = User_Trip_Booking.objects.filter(id=pk, user=user_id).first()
            post_inst.razorpay_id = razorpay_id
            post_inst.trip_cart_status = status
            post_inst.save()

            return Response({"message": "Trip has been booked Sucessfully"})

        except:
            return Response(
                {"message": "Invalid request"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def destroy(self, request, pk=None):
        user_id = request.GET.get("user_id", None)
        book_id = request.GET.get("book_id", None)

        if user_id is None:
            return Response(
                {"message": "Please provide user_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_post_inst = User_Trip_Booking.objects.filter(id=pk,user=user_id).first()
            scm_post_inst.delete()
            return Response(
                {"message": "Trip Booking Removed Successfully"},
                status=status.HTTP_200_OK,
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)

class TripInvoiceGenerateViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        tb = User_Trip_Booking.objects.get(id=pk)
        pdf = html_to_pdf('trip_invoice.html', {
            'pagesize': 'A4',
            'invoice_id': pk,
            'tb': tb,
            })

        return HttpResponse(pdf, content_type='application/pdf')

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


class UserGuideBookingViewSet(viewsets.ViewSet):
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
                            "guider_name": user_inst.guider_name,
                            "guider_mobile": user_inst.guider_mobile,
                            "rating": user_inst.rating,
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
        booking_date = request.POST.get("booking_date", None)
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
            booking_date=booking_date,
            guide_amount=guide_amount,
        )
        users_inst.save()

        users_data = serializers.UserGuideBookingSerializer(
            User_Guide_Booking.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        razorpay_id = request.POST.get("razorpay_id", None)
        booking_status = request.POST.get("booking_status", None)

        if pk is None and user_id is None:
            return Response(
                {"message": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = User_Guide_Booking.objects.get(id=pk)
            post_inst.razorpay_id = razorpay_id
            post_inst.status = booking_status
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Tour Guide has been booked Sucessfully"},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Invalid request"},
                status=status.HTTP_400_BAD_REQUEST,
            )


###########"""" HOTSPOTS """"""#######


class UserHotspotsCartViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_hotel = User_Hotspots_Cart.objects.filter(user=user_id)
            account_data_dic = serializers.UserHotspotsCartSerializer(
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
            created_user_id = account_data_dic.data[i].get("hostpots_id")
            try:
                user_inst = Hot_Spots.objects.get(id=created_user_id)

                account_data_dic.data[i].update(
                    {
                        "hostpots_id": {
                            "id": user_inst.id,
                            "title": user_inst.title,
                            "sub_title": user_inst.sub_title,
                            "city": user_inst.city,
                            "state": user_inst.state,
                            "pin_code": user_inst.pin_code,
                            "geo_location": user_inst.geo_location,
                            "amenites": user_inst.amenites,
                            "history": user_inst.history,
                            "about": user_inst.about,
                            "entry_fee": user_inst.entry_fee,
                            "parking_fee": user_inst.parking_fee,
                            "rating": user_inst.rating,
                            "tags": user_inst.tags,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {
                        "hostpots_id": {
                            "id": created_user_id,
                            "message": "Deleted Clients",
                        }
                    }
                )
        return Response(account_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        hostpots_id = request.POST.get("hostpots_id", None)
        no_guests = request.POST.get("no_guests", None)
        booking_date = request.POST.get("booking_date", None)
        cart_amount = request.POST.get("cart_amount", None)
        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            hotspots_inst = Hot_Spots.objects.get(id=hostpots_id)
        except:

            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = User_Hotspots_Cart.objects.create(
            user=user_inst,
            hostpots_id=hotspots_inst,
            no_guests=no_guests,
            booking_date=booking_date,
            cart_amount=cart_amount,
        )
        users_inst.save()

        users_data = serializers.UserHotspotsCartSerializer(
            User_Hotspots_Cart.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        cart_id = request.POST.get("cart_id", None)
        cart_status = request.POST.get("cart_status", None)

        if pk is None and user_id is None:
            return Response(
                {"message": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = User_Hotspots_Cart.objects.get(id=pk)
            post_inst.status = cart_status
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Hotspots Cart Updated Sucessfully"},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Sorry No data found with this cart id"},
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
            scm_post_inst = User_Hotspots_Cart.objects.filter(id=pk)
            scm_post_inst.delete()
            return Response(
                {"message": "Successfully Cart Removed"}, status=status.HTTP_200_OK
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)


class UserHotSpotsBookingViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.GET.get("user_id", None)
        try:
            sm_hotel = User_Hotspots_Bookings.objects.filter(user=user_id)
            account_data_dic = serializers.UserHotspotsBookingsSerializer(
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
            created_user_id = account_data_dic.data[i].get("cart_id")
            try:
                user_inst = User_Hotspots_Cart.objects.get(id=created_user_id)

                account_data_dic.data[i].update(
                    {
                        "cart_id": {
                            "id": user_inst.id,
                            "no_guests": user_inst.no_guests,
                            "cart_amount": user_inst.cart_amount,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {"cart_id": {"id": created_user_id, "message": "Deleted HotSpots"}}
                )
        return Response(account_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        user_id = request.POST.get("user_id", None)
        cart_id = request.POST.get("cart_id", None)
        no_guests = request.POST.get("no_guests", None)
        booking_date = request.POST.get("booking_date", None)
        booking_amount = request.POST.get("booking_amount", None)
        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
            cart_inst = User_Hotspots_Cart.objects.get(id=cart_id)
        except:

            return Response(
                {"message": "Invalid Request !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = User_Hotspots_Bookings.objects.create(
            user=user_inst,
            cart_id=cart_inst,
            no_guests=no_guests,
            booking_date=booking_date,
            booking_amount=booking_amount,
        )
        users_inst.save()

        users_data = serializers.UserHotspotsBookingsSerializer(
            User_Hotspots_Bookings.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        razorpay_id = request.POST.get("razorpay_id", None)
        booking_status = request.POST.get("booking_status", None)

        if pk is None and user_id is None:
            return Response(
                {"message": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            post_inst = User_Hotspots_Bookings.objects.get(id=pk)
            post_inst.razorpay_id = razorpay_id
            post_inst.status = booking_status
            post_inst.is_edited = True
            post_inst.save()

            return Response(
                {"message": "Tour HotSpots has been booked Sucessfully"},
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {"message": "Invalid request"},
                status=status.HTTP_400_BAD_REQUEST,
            )


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


class AllUserGuideBookingViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_hotel = User_Guide_Booking.objects.all()
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
                            "guider_name": user_inst.guider_name,
                            "guider_mobile": user_inst.guider_mobile,
                            "rating": user_inst.rating,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {"guide_id": {"id": created_user_id, "message": "Deleted Guide"}}
                )
        return Response(account_data_dic.data, status=status.HTTP_200_OK)


class AllUserHotspotsCartViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_hotel = User_Hotspots_Cart.objects.all()
            account_data_dic = serializers.UserHotspotsCartSerializer(
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
            created_user_id = account_data_dic.data[i].get("hostpots_id")
            try:
                user_inst = Hot_Spots.objects.get(id=created_user_id)

                account_data_dic.data[i].update(
                    {
                        "hostpots_id": {
                            "id": user_inst.id,
                            "title": user_inst.title,
                            "sub_title": user_inst.sub_title,
                            "city": user_inst.city,
                            "state": user_inst.state,
                            "pin_code": user_inst.pin_code,
                            "geo_location": user_inst.geo_location,
                            "amenites": user_inst.amenites,
                            "history": user_inst.history,
                            "about": user_inst.about,
                            "entry_fee": user_inst.entry_fee,
                            "parking_fee": user_inst.parking_fee,
                            "rating": user_inst.rating,
                            "tags": user_inst.tags,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {
                        "hostpots_id": {
                            "id": created_user_id,
                            "message": "Deleted Clients",
                        }
                    }
                )
        return Response(account_data_dic.data, status=status.HTTP_200_OK)


class AllUserHotSpotsBookingViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_hotel = User_Hotspots_Bookings.objects.all()
            account_data_dic = serializers.UserHotspotsBookingsSerializer(
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
            created_user_id = account_data_dic.data[i].get("cart_id")
            try:
                user_inst = User_Hotspots_Cart.objects.get(id=created_user_id)

                account_data_dic.data[i].update(
                    {
                        "cart_id": {
                            "id": user_inst.id,
                            "no_guests": user_inst.no_guests,
                            "cart_amount": user_inst.cart_amount,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {"cart_id": {"id": created_user_id, "message": "Deleted HotSpots"}}
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


class MyUserGuideBookingViewSet(viewsets.ViewSet):
    def list(self, request):
        client_id = request.GET.get("client_id", None)
        try:
            sm_hotel = User_Guide_Booking.objects.filter(client_id=client_id)
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
                            "guider_name": user_inst.guider_name,
                            "guider_mobile": user_inst.guider_mobile,
                            "rating": user_inst.rating,
                        }
                    }
                )
            except:
                account_data_dic.data[i].update(
                    {"guide_id": {"id": created_user_id, "message": "Deleted Guide"}}
                )
        return Response(account_data_dic.data, status=status.HTTP_200_OK)
