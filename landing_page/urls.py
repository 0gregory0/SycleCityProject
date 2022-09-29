from django.conf import settings
from django.urls import path
from .views import BikeRentingPage, LandingPage
from django.views import static

#Giving the landing page view a URL
urlpatterns = [
    path("", LandingPage.as_view(), name = "Landing Page"),
    path("rent/", BikeRentingPage.as_view(), name = "Bike Renting Page"),
]
