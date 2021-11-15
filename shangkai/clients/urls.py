from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()

# # """"HOTELS"""
router.register("client_register", views.UserRegisterViewSet, basename="ClientsRegister")
router.register(
    "hotel_registration", views.HotelRegistrationViewSet, basename="HotelRegistration"
)
router.register(
    "room_registration", views.RoomRegistrationViewSet, basename="RoomRegistration"
)


urlpatterns = [
    path("", include(router.urls)),
]
