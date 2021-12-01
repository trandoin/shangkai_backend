from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets
from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers


"""Model Package """
from .models import (
   About_Us,
   Footer_Copyright,
   Hotspot_Category,
   Hot_Spots,
   Comments_All,
   Payment_Transaction,
   Hotel_Category,
   My_Trips,
   My_Trips_Days,
)

"""Model Package """
from users.models import (
    Normal_UserReg,
   
)


class AboutUsViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_about_us = About_Us.objects.filter(status="1")
            about_us_data_dic = serializers.AboutUsSerializer(sm_about_us, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(about_us_data_dic.data, status=status.HTTP_200_OK)

class FooterViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_footer = Footer_Copyright.objects.filter(status="1")
            footer_data_dic = serializers.FooterSerializer(sm_footer, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(footer_data_dic.data, status=status.HTTP_200_OK)

class HotelCategoryViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_hotspots_cat = Hotel_Category.objects.filter(status="1")
            hotspots_cat_data_dic = serializers.HotelCategorySerializer(sm_hotspots_cat, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(hotspots_cat_data_dic.data, status=status.HTTP_200_OK)

class HotspotCategoryViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_hotspots_cat = Hotspot_Category.objects.filter(status="1")
            hotspots_cat_data_dic = serializers.HotspotCategorySerializer(sm_hotspots_cat, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(hotspots_cat_data_dic.data, status=status.HTTP_200_OK)

class HotSpotsViewSet(viewsets.ViewSet):
    def list(self, request):
        hotspot_cat = request.POST.get("hotspot_cat", None)
        hotspot_city = request.POST.get("hotspot_city", None)
        hotspot_price = request.POST.get("hotspot_price", None)

        if hotspot_cat is not None and hotspot_city is not None and hotspot_price is not None :
            sm_hotspots = Hot_Spots.objects.filter(category=hotspot_cat,city=hotspot_city,entry_fee=hotspot_price)
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        elif hotspot_cat is not None and hotspot_city is not None :
            sm_hotspots = Hot_Spots.objects.filter(category=hotspot_cat,city=hotspot_city)
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True) 
        elif hotspot_city is not None and hotspot_price is not None :
            sm_hotspots = Hot_Spots.objects.filter(city=hotspot_city,entry_fee=hotspot_price)
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        elif hotspot_cat is not None and hotspot_price is not None :
            sm_hotspots = Hot_Spots.objects.filter(category=hotspot_cat,entry_fee=hotspot_price)
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)           
        elif hotspot_cat is not None :
            sm_hotspots = Hot_Spots.objects.filter(category=hotspot_cat)
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        elif hotspot_city is not None :
            sm_hotspots = Hot_Spots.objects.filter(city=hotspot_city)
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        elif hotspot_price is not None :
            sm_hotspots = Hot_Spots.objects.filter(entry_fee=hotspot_price)
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)           
        else:
            sm_hotspots = Hot_Spots.objects.all()
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)


        return Response(hotspots_data_dic.data, status=status.HTTP_200_OK)

####  """""""" MY TRIPS """"""""######

class MyTripsViewSet(viewsets.ViewSet):
    def list(self, request):

        sm_mytrips_all = My_Trips.objects.all()
        mytrips_all_data_dic = serializers.MyTripsSerializer(sm_mytrips_all, many=True)
        for i in range(0, len(mytrips_all_data_dic.data)):
            created_hotspots_id = mytrips_all_data_dic.data[i].get("hotspots_id")
            # try:
            #     hotspots_inst = Hot_Spots.objects.get(id=created_hotspots_id)

            #     mytrips_all_data_dic.data[i].update(
            #         {
            #             "hotspots_id": {
            #                 "id": hotspots_inst.id,
            #                 "title": hotspots_inst.title,
            #                 "images": hotspots_inst.images,
            #             }
            #         }
            #     )
            # except:
            #     mytrips_all_data_dic.data[i].update(
            #         {"hotspots_id": {"id": created_hotspots_id, "message": "No HotSpots Found !"}}
            #     )  
            likes_user = Hot_Spots.objects.filter(id__in=mytrips_all_data_dic)
            for j in likes_user:
                hotspots.append({"id": j.id, "user_name": j.title})

            mytrips_all_data_dic.data[i].update({"likes": hotspots})      
        return Response(mytrips_all_data_dic.data, status=status.HTTP_200_OK)


class CommentsAllViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_comments_all = Comments_All.objects.filter(status="1")
            comments_all_data_dic = serializers.CommentsAllSerializer(sm_comments_all, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for i in range(0, len(comments_all_data_dic.data)):
            created_user_id = comments_all_data_dic.data[i].get("user")
            try:
                user_inst = Normal_UserReg.objects.get(id=created_user_id)

                comments_all_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                comments_all_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                )    
        return Response(comments_all_data_dic.data, status=status.HTTP_200_OK)


    def create(self, request):

        user_id = request.POST.get("user_id", None)
        post_id = request.POST.get("post_id", None)
        comments = request.POST.get("comments", None)
        comment_type = request.POST.get("comment_type", None)

        try:
            user_inst = Normal_UserReg.objects.get(id=user_id)
        except:

            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        users_inst = Comments_All.objects.create(
            user=user_inst,
            post_id=post_id,
            comments=comments,
            comment_type=comment_type,

        )
        users_inst.save()

        users_data = serializers.CommentsAllSerializer(
            Comments_All.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

class PaymentTransactionViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_payment_tra = Payment_Transaction.objects.filter(status="1")
            payment_tra_data_dic = serializers.PaymentTransactionAllSerializer(sm_payment_tra, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(payment_tra_data_dic.data, status=status.HTTP_200_OK)


#################  SEARCH HOTSPOTS ##########################   


class HotSpotSearchViewSet(viewsets.ViewSet):

    def list(self, request):
        title = request.GET.get("title", None)
        try:
            sm_hotspots = Hot_Spots.objects.filter(title=title)
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        except:
            return Response(
                {"message": "Sorry No Hotspots found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(hotspots_data_dic.data, status=status.HTTP_200_OK)

class HotSpotSearchByCatIdViewSet(viewsets.ViewSet):

    def list(self, request):
        category = request.GET.get("category_id", None)
        try:
            sm_cabs = Hot_Spots.objects.filter(category=category)
            cabs_data_dic = serializers.HotSpotsSerializer(sm_cabs, many=True)
        except:
            return Response(
                {"message": "Sorry No Hotspots found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(cabs_data_dic.data, status=status.HTTP_200_OK)        

