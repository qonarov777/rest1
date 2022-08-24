from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from .models import AboutUs
from .serializers import AboutUsSerializer
from .models import Homepage
from .serializers import HomepageSerializer

class ListCreateAboutUs(ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser]

class ListCreateHomepage(ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser]