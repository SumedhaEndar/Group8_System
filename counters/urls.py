from django.urls import path
from . import views

urlpatterns = [
    path("counter-home", views.home, name ="counter-home"),
]