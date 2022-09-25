from django.urls import path
from .views import LandingPage

#Giving the landing page view a URL
urlpatterns = [
    path("", LandingPage.as_view(), name = "Landing Page"),
]