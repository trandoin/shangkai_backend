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

        try:
            sm_hotspots = Hot_Spots.objects.filter(status="1")
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(hotspots_data_dic.data, status=status.HTTP_200_OK)

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
        return Response(comments_all_data_dic.data, status=status.HTTP_200_OK)

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