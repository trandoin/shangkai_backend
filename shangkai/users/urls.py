from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()

# # """"BOOKINGS"""
router.register("user_register", views.UserRegisterViewSet, basename="NormalUsersRegister")
router.register("hotel_booking", views.HotelBookingViewSet, basename="HotelBooking")


urlpatterns = [
    path("", include(router.urls)),
]