from datetime import datetime
import uuid
import requests

from shangkai_app.helpers import html_to_pdf
from shangkai_app.razorpay import verify_payment
from users.helpers import send_trek_book_email
from users.models import (
    Normal_UserReg,
)
from .razorpay import verify_payment,client
from clients.models import User_Register

# Create your views here.
from rest_framework import serializers, viewsets
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from . import serializers
import os
from dotenv import load_dotenv
load_dotenv()

"""Model Package """
from .models import (
    About_Us,
    Blog_Category,
    Blog_Post,
    BlogPost_Comments,
    Coupon,
    Footer_Copyright,
    HotSpot_Images,
    Hotspot_Category,
    Hot_Spots,
    Comments_All,
    Payment_Transaction,
    Hotel_Category,
    My_Trips,
    My_Trips_Days,
    Admin_Notification,
    Contact_Us,
    Tracking,
    Tracking_Bookings,
    Tracking_Order,
)

"""Model Package """


class AboutUsViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_about_us = About_Us.objects.filter(status="1")
            about_us_data_dic = serializers.AboutUsSerializer(
                sm_about_us, many=True)
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
            footer_data_dic = serializers.FooterSerializer(
                sm_footer, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(footer_data_dic.data, status=status.HTTP_200_OK)


####### BLOG SECTION #########


class BlogCategoryViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_category = Blog_Category.objects.all()
            category_data_dic = serializers.BlogCategorySerializer(
                sm_category, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(category_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):
        user_id = request.POST.get("user_id", None)
        title = request.POST.get("title", None)
        try:
            user_inst = User_Register.objects.get(id=user_id)
        except:
            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        cat_inst = Blog_Category.objects.create(
            title=title,
            user=user_inst,
        )
        cat_inst.save()

        cat_data = serializers.BlogCategorySerializer(
            Blog_Category.objects.filter(id=cat_inst.id), many=True
        )
        return Response(cat_data.data[0], status=status.HTTP_200_OK)


class BlogPostViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_posts = Blog_Post.objects.all()
            posts_data_dic = serializers.BlogPostSerializer(
                sm_posts, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(posts_data_dic.data)):
            created_user_id = posts_data_dic.data[i].get("user")
            try:
                user_inst = User_Register.objects.get(id=created_user_id)

                posts_data_dic.data[i].update(
                    {
                        "user": {
                            "id": user_inst.id,
                            "user_id": user_inst.user_id,
                            "user_name": user_inst.name,
                        }
                    }
                )
            except:
                posts_data_dic.data[i].update(
                    {"user": {"id": created_user_id, "message": "Deleted Account"}}
                ) 
            created_cat_id = posts_data_dic.data[i].get("category")
            try:
                cat_inst = Blog_Category.objects.get(id=created_cat_id)

                posts_data_dic.data[i].update(
                    {
                        "category": {
                            "id": cat_inst.id,
                            "cat_name": cat_inst.title,
                        }
                    }
                )
            except:
                posts_data_dic.data[i].update(
                    {
                        "category": {
                            "id": created_cat_id,
                            "message": "Deleted Category",
                        }
                    }
                )                                          
        return Response(posts_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):
        user_id = request.POST.get("user_id", None)
        category = request.POST.get("category", None)
        title = request.POST.get("title", None)
        text = request.POST.get("text", None)
        feature_image = request.POST.get("feature_image", None)
        try:
            user_inst = User_Register.objects.get(id=user_id)
            cate_inst = Blog_Category.objects.get(id=category)

        except:

            return Response(
                {"message": "No user found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        cat_inst = Blog_Post.objects.create(
            user=user_inst,
            category=cate_inst,
            title=title,
            text=text,
            feature_image=feature_image,
        )
        cat_inst.save()

        cat_data = serializers.BlogPostSerializer(
            Blog_Post.objects.filter(id=cat_inst.id), many=True
        )
        return Response(cat_data.data[0], status=status.HTTP_200_OK)


class BlogPostCommentsViewSet(viewsets.ViewSet):
    def list(self, request):
        post_id = request.GET.get("post_id", None)
        try:
            sm_comments = BlogPost_Comments.objects.filter(post=post_id)
            comments_data_dic = serializers.BlogPostCommentsSerializer(
                sm_comments, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )            
        return Response(comments_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):
        post = request.POST.get("post_id", None)
        user_ip = request.POST.get("user_ip", None)
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        comments = request.POST.get("comments", None)
        try:
            post_inst = Blog_Post.objects.get(id=post)

        except:

            return Response(
                {"message": "No Post found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        cat_inst = BlogPost_Comments.objects.create(
            post=post_inst,
            user_ip=user_ip,
            name=name,
            email=email,
            comments=comments,
        )
        cat_inst.save()

        cat_data = serializers.BlogPostCommentsSerializer(
            BlogPost_Comments.objects.filter(id=cat_inst.id), many=True
        )
        return Response(cat_data.data[0], status=status.HTTP_200_OK)


class ContactUsViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_contact = Contact_Us.objects.all()
            contact_data_dic = serializers.ContactUsSerializer(
                sm_contact, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(contact_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):
        datetime = request.POST.get("datetime", None)
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        mobile = request.POST.get("mobile", None)
        message = request.POST.get("message", None)

        contact_inst = Contact_Us.objects.create(
            datetime=datetime,
            name=name,
            email=email,
            mobile_num=mobile,
            message=message,
        )
        contact_inst.save()

        contact_data = serializers.ContactUsSerializer(
            Contact_Us.objects.filter(id=contact_inst.id), many=True
        )
        return Response(contact_data.data[0], status=status.HTTP_200_OK)


class NotificationViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_notification = Admin_Notification.objects.all()
            notification_data_dic = serializers.NotificationSerializer(
                sm_notification, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(notification_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):
        datetime = request.POST.get("datetime", None)
        title = request.POST.get("title", None)
        message = request.POST.get("message", None)

        notification_inst = Admin_Notification.objects.create(
            datetime=datetime,
            title=title,
            message=message,
        )
        notification_inst.save()

        notification_data = serializers.NotificationSerializer(
            Admin_Notification.objects.filter(id=notification_inst.id), many=True
        )
        return Response(notification_data.data[0], status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        notification_id = request.GET.get("notification_id", None)

        if notification_id is None:
            return Response(
                {"message": "Please provide notification_id"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            scm_notifi_inst = Admin_Notification.objects.filter(id=pk)
            scm_notifi_inst.delete()
            return Response(
                {"message": "Notification Deleted Successfully"},
                status=status.HTTP_200_OK,
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)


class HotelCategoryViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_hotspots_cat = Hotel_Category.objects.filter(status='1')
            hotspots_cat_data_dic = serializers.HotelCategorySerializer(
                sm_hotspots_cat, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(hotspots_cat_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        title = request.POST.get("title", None)

        hotels_inst = Hotel_Category.objects.create(
            title=title,
        )
        hotels_inst.save()

        hotels_data = serializers.HotelCategorySerializer(
            Hotel_Category.objects.filter(id=hotels_inst.id), many=True
        )
        return Response(hotels_data.data[0], status=status.HTTP_200_OK)


class HotspotCategoryViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_hotspots_cat = Hotspot_Category.objects.all()
            hotspots_cat_data_dic = serializers.HotspotCategorySerializer(
                sm_hotspots_cat, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(hotspots_cat_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        title = request.POST.get("title", None)
        sub_title = request.POST.get("sub_title", None)
        tagline = request.POST.get("tagline", None)
        images = request.POST.get("images", None)

        hotspots_cat_inst = Hotspot_Category.objects.create(
            title=title,
            sub_title=sub_title,
            tagline=tagline,
            images=images,
        )
        hotspots_cat_inst.save()

        hotspots_cat_data = serializers.HotspotCategorySerializer(
            Hotspot_Category.objects.filter(id=hotspots_cat_inst.id), many=True
        )
        return Response(hotspots_cat_data.data[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        status = request.GET.get("status", None)

        if pk is None:
            return Response({"message": "Invalid Request"})

        try:
            post_inst = Hotspot_Category.objects.get(id=pk)
            post_inst.status = status

            post_inst.is_edited = True
            post_inst.save()

            return Response({"message": "HotSpots Category Status Updated Sucessfully"})

        except:
            return Response({"message": "Something went to wrong ! Try again !"})


class HotSpotsViewSet(viewsets.ViewSet):
    def list(self, request):
        hotspot_cat = request.POST.get("hotspot_cat", None)
        hotspot_city = request.POST.get("hotspot_city", None)
        hotspot_price = request.POST.get("hotspot_price", None)

        if (
            hotspot_cat is not None
            and hotspot_city is not None
            and hotspot_price is not None
        ):
            sm_hotspots = Hot_Spots.objects.filter(
                category=hotspot_cat, city=hotspot_city, entry_fee=hotspot_price
            )
            hotspots_data_dic = serializers.HotSpotsSerializer(
                sm_hotspots, many=True)
        elif hotspot_cat is not None and hotspot_city is not None:
            sm_hotspots = Hot_Spots.objects.filter(
                category=hotspot_cat, city=hotspot_city
            )
            hotspots_data_dic = serializers.HotSpotsSerializer(
                sm_hotspots, many=True)
        elif hotspot_city is not None and hotspot_price is not None:
            sm_hotspots = Hot_Spots.objects.filter(
                city=hotspot_city, entry_fee=hotspot_price
            )
            hotspots_data_dic = serializers.HotSpotsSerializer(
                sm_hotspots, many=True)
        elif hotspot_cat is not None and hotspot_price is not None:
            sm_hotspots = Hot_Spots.objects.filter(
                category=hotspot_cat, entry_fee=hotspot_price
            )
            hotspots_data_dic = serializers.HotSpotsSerializer(
                sm_hotspots, many=True)
        elif hotspot_cat is not None:
            sm_hotspots = Hot_Spots.objects.filter(category=hotspot_cat)
            hotspots_data_dic = serializers.HotSpotsSerializer(
                sm_hotspots, many=True)
        elif hotspot_city is not None:
            sm_hotspots = Hot_Spots.objects.filter(city=hotspot_city)
            hotspots_data_dic = serializers.HotSpotsSerializer(
                sm_hotspots, many=True)
        elif hotspot_price is not None:
            sm_hotspots = Hot_Spots.objects.filter(entry_fee=hotspot_price)
            hotspots_data_dic = serializers.HotSpotsSerializer(
                sm_hotspots, many=True)
        else:
            sm_hotspots = Hot_Spots.objects.all()
            hotspots_data_dic = serializers.HotSpotsSerializer(
                sm_hotspots, many=True)

        return Response(hotspots_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.HotSpotsCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        status = request.GET.get("status", None)

        if pk is None:
            return Response({"message": "Invalid Request"})

        try:
            post_inst = Hot_Spots.objects.get(id=pk)
            post_inst.status = status

            post_inst.is_edited = True
            post_inst.save()

            return Response({"message": "HotSpots Status Updated Sucessfully"})

        except:
            return Response({"message": "Something went to wrong ! Try again !"})
class HotSpotsImageViewset(viewsets.ViewSet):
    def create(self, request):
        serializer = serializers.HotSpotImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        try:
            image = HotSpot_Images.objects.get(id=pk)
            image.delete()
            return Response({"message": "Image Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "Something went to wrong ! Try again !"},status=status.HTTP_400_BAD_REQUEST)
        
class TrackingViewSet(viewsets.ViewSet):
    def list(self, request):
        sm_tracking = Tracking.objects.filter(booking_upto__gte=datetime.now(),booking_start__lte=datetime.now())
        tracking_data_dic = serializers.TrackingSerializer(
            sm_tracking, many=True)

        return Response(tracking_data_dic.data, status=status.HTTP_200_OK)
    def create(self, request):
        tracking_serializer = serializers.TrackingSerializer(data=request.data)
        if tracking_serializer.is_valid():
            tracking_serializer.save()
            return Response(tracking_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tracking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk=None):
        tracking_inst = Tracking.objects.get(id=pk)
        tracking_serializer = serializers.TrackingSerializer(tracking_inst, data=request.data,partial=True)
        if tracking_serializer.is_valid():
            tracking_serializer.save()
            return Response(tracking_serializer.data, status=status.HTTP_200_OK)
        return Response(tracking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        try:
            tracking_inst = Tracking.objects.get(id=pk)
            tracking_inst.delete()
        except:
            return Response({"message": "Something went to wrong ! Try again !"})
        return Response({"message": "Tracking Deleted Sucessfully"},status=status.HTTP_204_NO_CONTENT)

class TrackingBookingViewSet(viewsets.ViewSet):
    def list(self, request):
        user_id = request.POST.get("user_id", None)
        sm_tracking_booking = Tracking_Bookings.objects.filter(user=user_id)
        tracking_booking_data_dic = serializers.TrackingBookingSerializer(
            sm_tracking_booking, many=True)
        return Response(tracking_booking_data_dic.data, status=status.HTTP_200_OK)
    def create(self, request):
        payment_id = request.POST.get("payment_id", "")
        order_id = request.POST.get("order_id", "")
        signature = request.POST.get("signature", "")
        user_id = request.POST.get("user_id", None)
        try:
            tracking_order_inst = Tracking_Order.objects.get(id=order_id)
            user_inst = Normal_UserReg.objects.get(id=user_id)
            tracking_inst = tracking_order_inst.tracking
        except:
            return Response({"message": "No User/Tracking found !"},status=status.HTTP_400_BAD_REQUEST,)
        """
        check if transaction id is valid
        """
        if verify_payment(payment_id, order_id, signature):
            if tracking_inst.seats - tracking_inst.booked >= int(tracking_order_inst.seats):
                tracking_inst.booked = tracking_inst.booked + int(tracking_order_inst.seats)
                tracking_inst.save()
                tracking_booking_inst = Tracking_Bookings.objects.create(
                    payment_id=payment_id,
                    order_id=order_id,
                    signature=signature,
                    user=user_inst,
                    tracking=tracking_inst,
                    seats=tracking_order_inst.seats,
                    amount=tracking_order_inst.amount,
                )
                #  send sms and email
                send_trek_book_email(
                    name=user_inst.name,
                    booking_id=tracking_booking_inst.id,
                    trek=tracking_inst.title,
                    start_date=tracking_inst.start_date.strftime("%d %b %Y, %I:%M %p"),
                    to=user_inst.mobile,
                    seats=tracking_order_inst.seats,
                    amount=str(tracking_order_inst.amount)[:-2],
                )
                #   send sms to user as a transactional message
                res = requests.post(
                    f"http://2factor.in/API/V1/{os.getenv('TWO_FACTOR_KEY')}/ADDON_SERVICES/SEND/TSMS",
                    data = {
                        "From": "SNGKAI",
                        "To": user_inst.mobile,
                        "TemplateName": "trek_booking",
                        "VAR1": user_inst.name,
                        "VAR2": tracking_inst.title,
                        "VAR3": order_id,
                        "VAR4": tracking_inst.start_date.strftime("%d %b %Y, %I:%M %p"),
                        "VAR5": tracking_order_inst.seats,
                        "VAR6": str(tracking_order_inst.amount)[:-2],
                        "VAR7": user_inst.mobile,
                    }
                )
                tracking_booking_data = serializers.TrackingBookingSerializer(
                    tracking_booking_inst
                )
                return Response(tracking_booking_data.data, status=status.HTTP_200_OK)
            return Response("not enough seats availaible", status=status.HTTP_400_BAD_REQUEST)
        return Response("not a valid payment", status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        stats = request.POST.get("status", None)
        try:
            tracking_booking_inst = Tracking_Bookings.objects.filter(id=pk,user=user_id).first()
        except:
            return Response({"message": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
        tracking_booking_serializer = serializers.TrackingBookingSerializer(tracking_booking_inst, data={"status":stats},partial=True)
        if tracking_booking_serializer.is_valid():
            tracking_booking_serializer.save()
            return Response(tracking_booking_serializer.data, status=status.HTTP_200_OK)
        return Response(tracking_booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        user_id = request.POST.get("user_id", None)
        try:
            tracking_booking_inst = Tracking_Bookings.objects.filter(id=pk,user=user_id).first()
            tracking_booking_inst.delete()
        except:
            return Response({"message": "Invalid Request"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Tracking Booking Deleted Sucessfully"},status=status.HTTP_204_NO_CONTENT)

class TreckingOrder(viewsets.ViewSet):
    def create(self,request):
        trecking_id = request.POST.get('trecking_id',None)
        try:
            trecking_inst = Tracking.objects.get(id=trecking_id)
        except:
            return Response({'status':False,'message':'Trecking not found'},status=400)
        seats = request.POST.get('seats',None)
        if trecking_inst.seats - trecking_inst.booked < int(seats):
            return Response("not enough seats availaible", status=status.HTTP_400_BAD_REQUEST)
        is_stay = request.POST.get('is_stay',0)
        is_student = request.POST.get('is_student',0)
        coupon_code = request.POST.get('coupon_code',None)
        currency = request.POST.get('currency', 'INR')
        if int(is_stay) == 1:
            if int(is_student) == 1:
                amount = int(trecking_inst.student_amount2) * int(seats)
            else:
                amount = int(trecking_inst.amount2) * int(seats)
        else:
            if int(is_student) == 1:
                amount = int(trecking_inst.student_amount) * int(seats)
            else:
                amount = int(trecking_inst.amount) * int(seats)
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
            Tracking_Order.objects.create(
                id = order['id'],
                seats = seats,
                is_stay = bool(int(is_stay)),
                is_student = bool(int(is_student)),
                currency = currency,
                amount = str(amount * 100),
                tracking = trecking_inst
                )
            return Response({"order":order,"coupon_applied":coupon_applied}, status=200)
        except Exception as e:
            print(e)
            return Response('error', status=500)

            
####  """""""" MY TRIPS """"""""######


class MyTripsViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_mytrips_all = My_Trips.objects.all()
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = []
        for trip in sm_mytrips_all:
            created_hotspots_ids = str(trip.hotspots_id)
            all_hotspots = created_hotspots_ids.split(",")
            serialized_data = serializers.MyTripsSerializer(trip).data
            serialized_data["hotspots"] = []
            for hostpot_id in all_hotspots:
                try:
                    hotspots_inst = Hot_Spots.objects.get(id=hostpot_id)
                    serialized_data["hotspots"].append(
                        {
                            "hotspot_id": str(hotspots_inst.id),
                            "title": hotspots_inst.title,
                            "sub_title": hotspots_inst.sub_title,
                            "title_image": hotspots_inst.title_image.url,
                            "city": hotspots_inst.city,
                            "state": hotspots_inst.state,
                            "about": hotspots_inst.about,
                        }
                    )
                except:
                    pass
            data.append(serialized_data)
        return Response(data, status=status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        try:
            trip = My_Trips.objects.get(id=pk)
        except:
            return Response(
                "Sorry No data found !",
                status=status.HTTP_400_BAD_REQUEST,
            )
        created_hotspots_ids = str(trip.hotspots_id)
        all_hotspots = created_hotspots_ids.split(",")
        serialized_data = serializers.MyTripsSerializer(trip).data
        serialized_data["hotspots"] = []
        for hostpot_id in all_hotspots:
            try:
                hotspots_inst = Hot_Spots.objects.get(id=hostpot_id)
                serialized_data["hotspots"].append(
                    {
                        "hotspot_id": str(hotspots_inst.id),
                        "title": hotspots_inst.title,
                        "sub_title": hotspots_inst.sub_title,
                        "title_image": hotspots_inst.title_image.url,
                        "city": hotspots_inst.city,
                        "state": hotspots_inst.state,
                        "about": hotspots_inst.about,
                    }
                )
            except:
                pass
        return Response(serialized_data, status=status.HTTP_200_OK)
    def create(self, request):

        title = request.POST.get("title", None)
        sub_title = request.POST.get("sub_title", None)
        category = request.POST.get("category", None)
        price = request.POST.get("price", None)
        offer_price = request.POST.get("offer_price", None)
        special_offer = request.POST.get("special_offer", None)
        deadline_date = request.POST.get("deadline_date", None)
        exlusion = request.POST.get("exlusion", None)
        description = request.POST.get("description", None)
        services = request.POST.get("services", None)
        hotspots_ids = request.POST.get("hotspots_id", None)
        includes = request.POST.get("includes", None)
        rules = request.POST.get("rules", None)
        days_no = request.POST.get("days_no", None)
        start_trip = request.POST.get("start_trip_date", None)

        trips_inst = My_Trips.objects.create(
            title=title,
            sub_title=sub_title,
            category=category,
            price=price,
            offer_price=offer_price,
            special_offer=special_offer,
            deadline_date=deadline_date,
            exlusion=exlusion,
            description=description,
            services=services,
            hotspots_id=hotspots_ids,
            includes=includes,
            rules=rules,
            days_no=days_no,
            start_trip=start_trip,
        )
        trips_inst.save()

        trips_data = serializers.MyTripsSerializer(
            My_Trips.objects.filter(id=trips_inst.id), many=True
        )
        return Response(trips_data.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        sttus = request.GET.get("status", None)

        if pk is None:
            return Response({"message": "Invalid Request"})

        try:
            post_inst = My_Trips.objects.get(id=pk)
            post_inst.status = sttus

            post_inst.is_edited = True
            post_inst.save()

            return Response({"message": "Trip Status Updated Sucessfully",
                           "trip":serializers.MyTripsSerializer(post_inst).data}, status=status.HTTP_200_OK)  

        except:
            return Response({"message": "Something went to wrong ! Try again !"},status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        try:
            post_inst = My_Trips.objects.get(id=pk)
            post_inst.delete()
        except:
            return Response({"message": "Invalid Request"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Trip Deleted Sucessfully"},status=status.HTTP_204_NO_CONTENT)

class MyTripsDaysViewSet(viewsets.ViewSet):
    def list(self, request):
        my_trip = request.GET.get("my_trip", None)
        try:
            sm_mytrips_all = My_Trips_Days.objects.filter(my_trip=my_trip)
            mytripsdays_all_data_dic = serializers.MyTripsDaysSerializer(
                sm_mytrips_all, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(mytripsdays_all_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        my_trip = request.POST.get("my_trip", None)
        description = request.POST.get("description", None)

        try:
            my_trips_inst = My_Trips.objects.get(id=my_trip)
        except:

            return Response(
                {"message": "No Trip found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        mytrips_days_inst = My_Trips_Days.objects.create(
            my_trip=my_trips_inst,
            description=description,
        )
        mytrips_days_inst.save()

        mytrips_days_data = serializers.MyTripsDaysSerializer(
            My_Trips_Days.objects.filter(id=mytrips_days_inst.id), many=True
        )
        return Response(mytrips_days_data.data[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        sttus = request.GET.get("status", None)

        if pk is None:
            return Response({"message": "Invalid Request"},status=status.HTTP_400_BAD_REQUEST)

        try:
            post_inst = My_Trips_Days.objects.get(id=pk)
            post_inst.status = sttus

            post_inst.is_edited = True
            post_inst.save()

            return Response({"message": "Trip Day Status Updated Sucessfully"},status=status.HTTP_200_OK)

        except:
            return Response({"message": "Something went to wrong ! Try again !"},status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        try:
            post_inst = My_Trips_Days.objects.get(id=pk)
            post_inst.delete()
        except:
            return Response({"message": "Invalid Request"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Trip Day Deleted Sucessfully"},status=status.HTTP_204_NO_CONTENT)

class AllMyTripsDaysViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            sm_mytrips_all = My_Trips_Days.objects.all()
            mytripsdays_all_data_dic = serializers.MyTripsDaysSerializer(
                sm_mytrips_all, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for i in range(0, len(mytripsdays_all_data_dic.data)):
            created_trip_id = mytripsdays_all_data_dic.data[i].get("my_trip")
            try:
                trip_inst = My_Trips.objects.get(id=created_trip_id)

                mytripsdays_all_data_dic.data[i].update(
                    {
                        "my_trip": {
                            "id": trip_inst.id,
                            "trip_title": trip_inst.title,
                        }
                    }
                )
            except:
                mytripsdays_all_data_dic.data[i].update(
                    {"my_trip": {"id": created_trip_id, "message": "Deleted Trip"}}
                )
        return Response(mytripsdays_all_data_dic.data, status=status.HTTP_200_OK)


class CommentsAllViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_comments_all = Comments_All.objects.filter(status="1")
            comments_all_data_dic = serializers.CommentsAllSerializer(
                sm_comments_all, many=True
            )
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
            payment_tra_data_dic = serializers.PaymentTransactionAllSerializer(
                sm_payment_tra, many=True
            )
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
        hotspot_id = request.GET.get("hotspot_id", None)

        if title is not None:
            sm_hotspots = Hot_Spots.objects.filter(title=title)
            hotspots_data_dic = serializers.HotSpotsSerializer(
                sm_hotspots, many=True)
        elif hotspot_id is not None:
            sm_hotspots = Hot_Spots.objects.filter(id=hotspot_id)
            hotspots_data_dic = serializers.HotSpotsSerializer(
                sm_hotspots, many=True)
        else:
            sm_hotspots = Hot_Spots.objects.all()
            hotspots_data_dic = serializers.HotSpotsSerializer(
                sm_hotspots, many=True)

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

class TrackingInvoiceGenerateViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        tb = Tracking_Bookings.objects.get(id=pk)
        pdf = html_to_pdf('tracking_invoice.html', {
            'pagesize': 'A4',
            'invoice_id': pk,
            'tb': tb,
            })

        return HttpResponse(pdf, content_type='application/pdf')