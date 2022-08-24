from .views import ListCreateAboutUs 
from django.urls import path
from .views import ListCreateHomepage

urlpatterns = [
    path('about/',ListCreateAboutUs.as_view()),
    path('home/',ListCreateHomepage.as_view()),
]
