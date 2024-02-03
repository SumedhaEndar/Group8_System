from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("plans/", views.plans, name="plans"),
    path("programs/", views.programs, name="programs"),
    path("fitness-locator/", views.fitnessLocator, name="fitness-locator"),
    path("contact-us/", views.contactUs, name="contact-us"),
]