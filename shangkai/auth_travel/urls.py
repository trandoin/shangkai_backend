from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()

# router.register('profile',views.profile,basename='profile')


urlpatterns = [
    path('',include(router.urls)),
    # path('login/',views.login_view),
]