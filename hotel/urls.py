from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, HotelPictureViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'hotel-pictures', HotelPictureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]