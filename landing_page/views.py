from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

#Landing Page View
class LandingPage (TemplateView):
    template_name = "landing_page/index.html"

#Bikes to Rent view
class BikeRentingPage (TemplateView):
    template_name = "landing_page/bikestorent.html"