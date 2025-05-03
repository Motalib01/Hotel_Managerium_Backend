from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Hotel, HotelPicture
from .serializers import HotelSerializer, HotelPictureSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()# pylint: disable=no-member
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated] 

class HotelPictureViewSet(viewsets.ModelViewSet):
    queryset = HotelPicture.objects.all()# pylint: disable=no-member
    serializer_class = HotelPictureSerializer
    permission_classes = [IsAuthenticated] 
