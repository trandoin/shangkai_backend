from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()

router.register("about_us", views.AboutUsViewSet, basename="AboutUs")
router.register("footer", views.FooterViewSet, basename="Footer")
router.register("category_hotspots", views.HotspotCategoryViewSet, basename="HotspotCategory")
router.register("hot_spots", views.HotSpotsViewSet, basename="HotSpots")
router.register("comments_all", views.CommentsAllViewSet, basename="CommentsAll")
router.register("payment_tra", views.PaymentTransactionViewSet, basename="PaymentTransaction")
router.register("hotspot_search", views.HotSpotSearchViewSet, basename="HotSpotsSearch")
router.register("hotspot_search_bycategory", views.HotSpotSearchByCatIdViewSet, basename="HotSpotsSearchCategory")


urlpatterns = [
    path("", include(router.urls)),
]
