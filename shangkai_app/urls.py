from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()

router.register("about_us", views.AboutUsViewSet, basename="AboutUs")
router.register("footer", views.FooterViewSet, basename="Footer")
router.register("contact_us", views.ContactUsViewSet, basename="ContactUs")
router.register("notification", views.NotificationViewSet, basename="Notification")
router.register("blog_category", views.BlogCategoryViewSet, basename="BlogCategory")
router.register("blog_post", views.BlogPostViewSet, basename="BlogPosts")
router.register("blog_comments", views.BlogPostCommentsViewSet, basename="BlogComments")

router.register(
    "category_hotspots", views.HotspotCategoryViewSet, basename="HotspotCategory"
)
router.register("hot_spots", views.HotSpotsViewSet, basename="HotSpots")
router.register("tracking", views.TrackingViewSet, basename="Tracking")
router.register("comments_all", views.CommentsAllViewSet, basename="CommentsAll")
router.register(
    "payment_tra", views.PaymentTransactionViewSet, basename="PaymentTransaction"
)
router.register("hotel_category", views.HotelCategoryViewSet, basename="HotelCategory")
router.register("hotspot_search", views.HotSpotSearchViewSet, basename="HotSpotsSearch")
router.register(
    "hotspot_search_bycategory",
    views.HotSpotSearchByCatIdViewSet,
    basename="HotSpotsSearchCategory",
)

##### """""""" MY TRIPS """"""""####
router.register("my_trips", views.MyTripsViewSet, basename="MYTrips")
router.register("my_trips_days", views.MyTripsDaysViewSet, basename="MYTripsDays")
router.register("all_trips_days", views.AllMyTripsDaysViewSet, basename="AllTripsDays")


urlpatterns = [
    path("", include(router.urls)),
]
