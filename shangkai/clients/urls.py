from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()


router.register("client_register", views.UserRegisterViewSet, basename="ClientsRegister")
router.register("client_login", views.ClientloginViewSet, basename="ClientsLogin")

# # """"HOTELS"""

router.register(
    "hotel_registration", views.HotelRegistrationViewSet, basename="HotelRegistration"
)
router.register(
    "room_registration", views.RoomRegistrationViewSet, basename="RoomRegistration"
)
router.register(
    "room_search", views.RoomSearchViewSet, basename="RoomSearch"
)
router.register(
    "get_hotel_by_id", views.GetHotelByCatIdViewSet, basename="GetHotelById"
)


##### CABS #####
router.register(
    "driver_registration", views.DriverRegistrationViewSet, basename="DriverRegistration"
)

router.register(
    "cab_registration", views.CabRegistrationViewSet, basename="CabRegistration"
)
router.register(
    "cab_search", views.CabSearchViewSet, basename="CabSearch"
)




urlpatterns = [
    path("", include(router.urls)),
]
