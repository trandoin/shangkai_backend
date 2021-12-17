from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()


router.register(
    "client_register", views.UserRegisterViewSet, basename="ClientsRegister"
)
router.register("client_login", views.ClientloginViewSet, basename="ClientsLogin")

# # """"HOTELS"""

router.register(
    "hotel_registration", views.HotelRegistrationViewSet, basename="HotelRegistration"
)
router.register(
    "room_registration", views.RoomRegistrationViewSet, basename="RoomRegistration"
)
router.register("room_search", views.RoomSearchViewSet, basename="RoomSearch")
router.register("room_get_byId", views.RoomGetByIdViewSet, basename="RoomGetById")
router.register(
    "get_hotel_by_id", views.GetHotelByCatIdViewSet, basename="GetHotelById"
)


##### CABS #####
router.register(
    "driver_registration",
    views.DriverRegistrationViewSet,
    basename="DriverRegistration",
)

router.register(
    "cab_registration", views.CabRegistrationViewSet, basename="CabRegistration"
)
router.register("cab_search", views.CabSearchViewSet, basename="CabSearch")
router.register(
    "cab_getby_locations", views.CabGetByLocationViewSet, basename="CabGetByLocation"
)

#######"""""" TOUR GUIDE  """"""#######
router.register("tour_location", views.TourLocationsViewSet, basename="TourLocations")
router.register("tour_packages", views.TourPackagesViewSet, basename="TourPackages")
router.register("my_tour_guider", views.TourGuiderViewSet, basename="TourGuider")


############# """""""" ADMIN """"""""##########

router.register("get_clients", views.GetClientslAllViewSet, basename="GetClientsAll")
router.register("get_hotels", views.GetHotelAllViewSet, basename="GetHotelAll")
router.register("get_rooms", views.GetRoomALLViewSet, basename="GetRoomALL")
router.register("get_cabs", views.GetCabAllViewSet, basename="GetCabAll")
router.register("get_drivers", views.GetDriverAllViewSet, basename="GetDriverAll")

router.register("all_tour_location", views.GetAllTourLocationsViewSet, basename="AllTourLocations")
router.register("all_tour_packages", views.GetAllTourPackagesViewSet, basename="AllTourPackages")
router.register("all_my_tour_guider", views.GetAllTourGuiderViewSet, basename="AllTourGuider")

urlpatterns = [
    path("", include(router.urls)),
]
