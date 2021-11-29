from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets
from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.
"""Model Package """
from .models import (
    Reg_Hotel,
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

        try:
            sm_users = User_Register.objects.filter(status="0")
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

        users_inst = User_Register.objects.create(
            user_id=user_id,
            user_ip=user_ip,
            name=name,
            email=email,
            mobile=mobile,
            password=password,
            image=image,
        )
        users_inst.save()

        users_data = serializers.UserRegisterSerializer(
            User_Register.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)


class ClientloginViewSet(viewsets.ViewSet):

    def create(self, request):

        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
         
        if email is None and password is None : 

            return Response(
                    {"message": "Enter username & password !"},
                    status=status.HTTP_400_BAD_REQUEST,
                )    

        try:
            users_inst = User_Register.objects.filter(email=email,password=password)
            users_data_dic = serializers.UserRegisterSerializer(
                users_inst, many=True
            )
        except:
            return Response(
                {"message": "Invalid username & password !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)


class HotelRegistrationViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.POST.get("user_id", None)
        # try:
        #     user_inst = User_Register.objects.get(id=user_id)
        # except:

        #     return Response(
        #         {"message": "No user found !"},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )
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
        # hotel_cat = request.POST.get("hotel_cat", None)
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
            # hotel_cat_inst = Hotel_Category.objects.get(id=hotel_cat)

        except:

            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        users_inst = Reg_Hotel.objects.create(
            user=user_inst,
            # hotel_cat=hotel_cat_inst,
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


class RoomRegistrationViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.POST.get("user_id", None)
        hotel_id = request.POST.get("hotel_id", None)

        try:
            sm_users = Room_Register.objects.filter(user=user_id,hotel_id=hotel_id)
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

class DriverRegistrationViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.POST.get("user_id", None)
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
        driver_doc = request.POST.get("driver_doc", None)
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
            driver_doc=driver_doc,
            picture=picture,
        )
        users_inst.save()

        users_data = serializers.DriverRegisterSerializer(
            Driver_Reg.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

class CabRegistrationViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.POST.get("user_id", None)
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
        car_doc = request.POST.get("car_doc", None)
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
            car_doc=car_doc,
            car_images=car_images,
        )
        users_inst.save()

        users_data = serializers.CabRegisterSerializer(
            Cabs_Reg.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)    



###############      SEARCH BAR  #######################

class CabSearchViewSet(viewsets.ViewSet):

    def list(self, request):
        cab_name = request.GET.get("cab_name", None)
        checkin_date = request.GET.get("checkin_date", None)
        checkout_date = request.GET.get("checkout_date", None)
        from_location = request.GET.get("from_location", None)
        destination = request.GET.get("destination", None)
        try:
            sm_cabs = Cabs_Reg.objects.filter(car_name=cab_name,checkin_date=checkin_date,checkout_date=checkout_date,pickup_point=from_location,destination=destination)
            cabs_data_dic = serializers.CabRegisterSerializer(sm_cabs, many=True)
        except:
            return Response(
                {"message": "Sorry No cab found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(cabs_data_dic.data, status=status.HTTP_200_OK)


class RoomSearchViewSet(viewsets.ViewSet):

    def list(self, request):
        room_type = request.GET.get("room_type", None)
        checkin_date = request.GET.get("checkin_date", None)
        checkout_date = request.GET.get("checkout_date", None)
        try:
            sm_cabs = Room_Register.objects.filter(room_type=room_type,checkin_date=checkin_date,checkout_date=checkout_date)
            cabs_data_dic = serializers.RoomRegisterSerializer(sm_cabs, many=True)
        except:
            return Response(
                {"message": "Sorry No cab found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(cabs_data_dic.data, status=status.HTTP_200_OK)

class GetHotelByCatIdViewSet(viewsets.ViewSet):
    def list(self, request):
        hotel_cat_id = request.POST.get("hotel_cat_id", None)

        try:
            sm_users = Reg_Hotel.objects.filter(hotel_cat=hotel_cat_id)
            users_data_dic = serializers.HotelRegisterSerializer(sm_users, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(users_data_dic.data, status=status.HTTP_200_OK)        
