from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()


router.register("user_register", views.UserRegisterViewSet, basename="NormalUsersRegister")
router.register("account_details", views.AccounDetailsBookingViewSet, basename="AccounDetailsBooking")

# # """"BOOKINGS"""
# router.register("hotel_booking", views.HotelBookingViewSet, basename="HotelBooking")
router.register("cab_booking", views.CabBookingViewSet, basename="CabBooking")


urlpatterns = [
    path("", include(router.urls)),
]