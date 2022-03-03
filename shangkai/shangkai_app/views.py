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
    Admin_Notification,
    Contact_Us,
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


####### BLOG SECTION #########

class BlogCategoryViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_category = Blog_Category.objects.all()
            category_data_dic = serializers.BlogCategorySerializer(sm_category, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(category_data_dic.data, status=status.HTTP_200_OK)

class BlogPostViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_posts = Blog_Post.objects.all()
            posts_data_dic = serializers.BlogPostSerializer(sm_posts, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(posts_data_dic.data, status=status.HTTP_200_OK)

class BlogPostCommentsViewSet(viewsets.ViewSet):
    def list(self, request):
        post_id = request.GET.get("post_id", None)
        try:
            sm_comments = BlogPost_Comments.objects.filter(post=post_id)
            comments_data_dic = serializers.BlogPostCommentsSerializer(sm_comments, many=True)
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(comments_data_dic.data, status=status.HTTP_200_OK)

class ContactUsViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_contact = Contact_Us.objects.all()
            contact_data_dic = serializers.ContactUsSerializer(sm_contact, many=True)
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
            notification_data_dic = serializers.NotificationSerializer(sm_notification, many=True)
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
                {"message": "Notification Deleted Successfully"}, status=status.HTTP_200_OK
            )
        except:
            return Response({"message": "Details not found"}, status=status.HTTP_200_OK)

class HotelCategoryViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_hotspots_cat = Hotel_Category.objects.all()
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
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        elif hotspot_cat is not None and hotspot_city is not None:
            sm_hotspots = Hot_Spots.objects.filter(
                category=hotspot_cat, city=hotspot_city
            )
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        elif hotspot_city is not None and hotspot_price is not None:
            sm_hotspots = Hot_Spots.objects.filter(
                city=hotspot_city, entry_fee=hotspot_price
            )
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        elif hotspot_cat is not None and hotspot_price is not None:
            sm_hotspots = Hot_Spots.objects.filter(
                category=hotspot_cat, entry_fee=hotspot_price
            )
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        elif hotspot_cat is not None:
            sm_hotspots = Hot_Spots.objects.filter(category=hotspot_cat)
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        elif hotspot_city is not None:
            sm_hotspots = Hot_Spots.objects.filter(city=hotspot_city)
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        elif hotspot_price is not None:
            sm_hotspots = Hot_Spots.objects.filter(entry_fee=hotspot_price)
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        else:
            sm_hotspots = Hot_Spots.objects.all()
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)

        return Response(hotspots_data_dic.data, status=status.HTTP_200_OK)

    def create(self, request):

        title = request.POST.get("title", None)
        sub_title = request.POST.get("sub_title", None)
        city = request.POST.get("city", None)
        state = request.POST.get("state", None)
        pin_code = request.POST.get("pin_code", None)
        geo_location = request.POST.get("geo_location", None)
        amenites = request.POST.get("amenites", None)
        history = request.POST.get("history", None)
        about = request.POST.get("about", None)
        images = request.POST.get("images", None)
        entry_fee = request.POST.get("entry_fee", None)
        parking_fee = request.POST.get("parking_fee", None)
        category = request.POST.get("category_id", None)
        rating = request.POST.get("rating", None)
        tags = request.POST.get("tags", None)

        try:
            cat_inst = Hotspot_Category.objects.get(id=category)
        except:

            return Response(
                {"message": "No Category found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users_inst = Hot_Spots.objects.create(
            title=title,
            sub_title=sub_title,
            city=city,
            state=state,
            pin_code=pin_code,
            geo_location=geo_location,
            amenites=amenites,
            history=history,
            about=about,
            images=images,
            entry_fee=entry_fee,
            parking_fee=parking_fee,
            category=cat_inst,
            rating=rating,
            tags=tags,
        )
        users_inst.save()

        users_data = serializers.HotSpotsSerializer(
            Hot_Spots.objects.filter(id=users_inst.id), many=True
        )
        return Response(users_data.data[0], status=status.HTTP_200_OK)

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

####  """""""" MY TRIPS """"""""######


class MyTripsViewSet(viewsets.ViewSet):
    def list(self, request):

        try:
            sm_mytrips_all = My_Trips.objects.all()
            mytrips_all_data_dic = serializers.MyTripsSerializer(
                sm_mytrips_all, many=True
            )
        except:
            return Response(
                {"message": "Sorry No data found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # for i in range(0, len(mytrips_all_data_dic.data)):
        #     created_hotspots_id = mytrips_all_data_dic.data[i].get("hotspots_id")
        #     try:
        #         hotspots_inst = Hot_Spots.objects.get(id=created_hotspots_id)

        #         mytrips_all_data_dic.data[i].update(
        #             {
        #                 "hotspots_id": {
        #                     "id": hotspots_inst.id,
        #                 }
        #             }
        #         )
        #     except:
        #         mytrips_all_data_dic.data[i].update(
        #             {
        #                 "hotspots_id": {
        #                     "id": created_hotspots_id,
        #                     "message": "No HotSpots Found !",
        #                 }
        #             }
        #         )
        return Response(mytrips_all_data_dic.data, status=status.HTTP_200_OK)

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
        status = request.GET.get("status", None)

        if pk is None:
            return Response({"message": "Invalid Request"})

        try:
            post_inst = My_Trips.objects.get(id=pk)
            post_inst.status = status

            post_inst.is_edited = True
            post_inst.save()

            return Response({"message": "Trip Status Updated Sucessfully"})

        except:
            return Response({"message": "Something went to wrong ! Try again !"}) 

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
                {"message": "No HotSpots found !"},
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
        status = request.GET.get("status", None)

        if pk is None:
            return Response({"message": "Invalid Request"})

        try:
            post_inst = My_Trips_Days.objects.get(id=pk)
            post_inst.status = status

            post_inst.is_edited = True
            post_inst.save()

            return Response({"message": "Trip Status Updated Sucessfully"})

        except:
            return Response({"message": "Something went to wrong ! Try again !"})
            

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
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        elif hotspot_id is not None:
            sm_hotspots = Hot_Spots.objects.filter(id=hotspot_id)
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)
        else:
            sm_hotspots = Hot_Spots.objects.all()
            hotspots_data_dic = serializers.HotSpotsSerializer(sm_hotspots, many=True)

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
