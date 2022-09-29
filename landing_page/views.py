from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#Landing Page View
class LandingPage (TemplateView):
    template_name = "landing_page/index.html"

#Bikes to Rent view
@csrf_exempt
class BikeRentingPage (TemplateView):
    template_name = "landing_page/bikestorent.html"