from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("programs/", views.programs, name="programs"),
    path("program-detail/<int:program_id>", views.program_detail, name="program-detail"),
    path("plans/", views.plans, name="plans"),
    path("fitness-locator/", views.fitnessLocator, name="fitness-locator"),
    path("contact-us/", views.contactUs, name="contact-us"),
]