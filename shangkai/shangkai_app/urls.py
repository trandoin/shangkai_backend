from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()

router.register("about_us", views.AboutUsViewSet, basename="AboutUs")
router.register("footer", views.FooterViewSet, basename="Footer")



urlpatterns = [
    path("", include(router.urls)),
]
