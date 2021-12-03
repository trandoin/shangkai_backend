from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()


router.register("user_register", views.UserRegisterViewSet, basename="NormalUsersRegister")
router.register("user_login", views.UserLoginViewSet, basename="NormalUsersLogin")
router.register("account_details", views.AccounDetailsBookingViewSet, basename="AccounDetailsBooking")

# # """"BOOKINGS"""
router.register("hotel_booking", views.HotelBookingViewSet, basename="HotelBooking")
router.register("cab_booking", views.CabBookingViewSet, basename="CabBooking")

#### """"""""CART """"""""###
router.register("hotel_cart", views.HotelCartViewSet, basename="HotelCart")
router.register("cab_cart", views.CabCartViewSet, basename="CabCart")
router.register("trips_cart", views.UserTripsCartViewSet, basename="TripsCart")

############ """""""""" PAYMENT """"""""######
router.register("hotel_payment", views.HotelPaymentViewSet, basename="HotelPayemnt")


################"""""""""" ADMIN """"""""""""""###########

router.register("get_users", views.GetAllUsersViewSet, basename="GetAllUsers")
router.register("get_users_hotelbooking", views.GetUsersHotelBookingViewSet, basename="GetUsersHotelBooking")
router.register("get_users_cabbooking", views.GetUsersCabBookingViewSet, basename="GetUsersCabBooking")
router.register("get_users_cabcart", views.GetUsersCabCartViewSet, basename="GetusersCabCart")
router.register("get_users_hotelcart", views.GetUsersHotelCartViewSet, basename="GetUsersHotelCart")
router.register("get_users_tripcart", views.GetUserTripsCartViewSet, basename="GetUserTripsCart")
router.register("get_users_booking_payments", views.GetUsersHotelPaymentViewSet, basename="GetUsersHotelPayment")



urlpatterns = [
    path("", include(router.urls)),
]