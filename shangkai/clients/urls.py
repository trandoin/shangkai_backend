from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()


router.register("client_register", views.UserRegisterViewSet, basename="ClientsRegister")

# # """"HOTELS"""

# router.register(
#     "hotel_registration", views.HotelRegistrationViewSet, basename="HotelRegistration"
# )
# router.register(
#     "room_registration", views.RoomRegistrationViewSet, basename="RoomRegistration"
# )

##### CABS #####
router.register(
    "driver_registration", views.DriverRegistrationViewSet, basename="DriverRegistration"
)

router.register(
    "cab_registration", views.CabRegistrationViewSet, basename="CabRegistration"
)


urlpatterns = [
    path("", include(router.urls)),
]
