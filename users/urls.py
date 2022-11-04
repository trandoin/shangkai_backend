from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()


router.register(
    "user_register", views.UserRegisterViewSet, basename="NormalUsersRegister"
)
router.register("user_login", views.UserLoginViewSet, basename="NormalUsersLogin")
router.register(
    "verify_email_user", views.UserVerifyEmailViewSet, basename="VerifyEmail"
)
router.register(
    "account_details",
    views.AccounDetailsBookingViewSet,
    basename="AccounDetailsBooking",
)
router.register(
    "user_ratings",
    views.UserRationsViewSet,
    basename="UserRations",
)
router.register(
    "user_password_update",
    views.UserUpdatePasswordViewSet,
    basename="UsersPasswordUpdate",
)


# # """"BOOKINGS"""
router.register("hotel_booking", views.HotelBookingViewSet, basename="HotelBooking")
router.register("cab_booking", views.CabBookingViewSet, basename="CabBooking")
router.register(
    "trip_booking", views.UserTripsBookingViewSet, basename="UserTripsBooking"
)
router.register(
    "my_hotspots_booking", views.UserHotSpotsBookingViewSet, basename="HotSpotsBookings"
)
router.register(
    "my_guide_booking", views.UserGuideBookingViewSet, basename="MyGuideBookings"
)

#########"""""""""""" MY Clients BOOKINGS """"""""############
router.register(
    "my_hotel_bookings", views.GetMyUsersHotelBookingViewSet, basename="MyHotelBookings"
)
router.register(
    "my_cabs_booking", views.GetMyUsersCabBookingViewSet, basename="MyCabBookings"
)
router.register(
    "user_guide_booking", views.MyUserGuideBookingViewSet, basename="MyGuideBookings"
)


#### """"""""CART """"""""###
router.register("hotel_cart", views.HotelCartViewSet, basename="HotelCart")
router.register("cab_cart", views.CabCartViewSet, basename="CabCart")
router.register("trips_cart", views.UserTripsCartViewSet, basename="TripsCart")
router.register("trip_invoice",views.TripInvoiceGenerateViewSet,basename="TripsInvoice")
router.register(
    "hotspots_cart", views.UserHotspotsCartViewSet, basename="HotSpotssCart"
)
router.register("guide_cart", views.UserGuideCartViewset, basename="GuideCart")


############ """""""""" PAYMENT """"""""######
router.register("hotel_order", views.HotelOrderViewSet, basename="HotelOrder")
router.register("trip_order",views.UserTripsOrderViewset,basename="TripsOrder")
router.register("guide_order", views.UserGuideOrderViewset, basename="GuideOrder")
router.register("hotel_payment", views.HotelPaymentViewSet, basename="HotelPayemnt")
router.register("cab_payment", views.CabPaymentViewSet, basename="CabPayemnt")
router.register("trip_payment", views.TripPaymentViewSet, basename="TripPayemnt")


################"""""""""" ADMIN """"""""""""""###########

router.register("get_users", views.GetAllUsersViewSet, basename="GetAllUsers")
router.register(
    "get_users_hotelbooking",
    views.GetUsersHotelBookingViewSet,
    basename="GetUsersHotelBooking",
)
router.register(
    "get_users_cabbooking",
    views.GetUsersCabBookingViewSet,
    basename="GetUsersCabBooking",
)
router.register(
    "get_users_tripbooking",
    views.UserAllTripsBookingViewSet,
    basename="UserTripsBooking",
)

router.register(
    "get_users_cabcart", views.GetUsersCabCartViewSet, basename="GetusersCabCart"
)
router.register(
    "get_users_hotelcart", views.GetUsersHotelCartViewSet, basename="GetUsersHotelCart"
)
router.register(
    "get_users_tripcart", views.GetUserTripsCartViewSet, basename="GetUserTripsCart"
)
router.register(
    "get_users_booking_payments",
    views.GetUsersHotelPaymentViewSet,
    basename="GetUsersHotelPayment",
)
router.register(
    "get_cabbooking_payment",
    views.GetAllCabPaymentViewSet,
    basename="GetUserCabPayment",
)
router.register(
    "get_tripbooking_payment",
    views.GetAllTripPaymentViewSet,
    basename="GetUserTripPayment",
)
router.register(
    "all_userhotspots_cart",
    views.AllUserHotspotsCartViewSet,
    basename="AllUserHotspotsCart",
)
router.register(
    "all_userhotspots_bookings",
    views.AllUserHotSpotsBookingViewSet,
    basename="UserHotSpotsBooking",
)
router.register(
    "all_userguide_bookings",
    views.AllUserGuideBookingViewSet,
    basename="AllUserGuideBooking",
)


urlpatterns = [
    path("", include(router.urls)),
]
