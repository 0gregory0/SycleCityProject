from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class LandingPage(TestCase): #Tests for the landing page

    #testing whether the url points to a page
    def test_correct_url_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    #testing whether the url is named correctly
    def test_url_name(self):
        response = self.client.get(reverse("Landing Page"))
        self.assertEqual(response.status_code, 200)

    #testing whether the correct template is being returned
    def test_url_template(self):
        response = self.client.get(reverse("Landing Page"))
        self.assertTemplateUsed(response, "landing_page\index.html")

    #testing whether our template has a specific content
    def test_template_content(self):
        response = self.client.get(reverse("Landing Page"))
        self.assertContains(response, "<h3>100+</h3>")


class BikeRentingPage(TestCase):

    #testing whether the url points to a page
    def test_correct_url_location(self):
        response = self.client.get("/rent/")
        self.assertEqual(response.status_code, 200)

    #testing whether the url is named correctly
    def test_url_name(self):
        response = self.client.get(reverse("Bike Renting Page"))
        self.assertEqual(response.status_code, 200)

    #testing whether the correct template is being returned
    def test_url_template(self):
        response = self.client.get(reverse("Bike Renting Page"))
        self.assertTemplateUsed(response, r"landing_page\bikestorent.html")

    #testing whether our template has a specific content
    def test_template_content(self):
        response = self.client.get(reverse("Bike Renting Page"))
        self.assertContains(response, "<h2>Call us at 0115501903, to rent the available bikes</h2>")