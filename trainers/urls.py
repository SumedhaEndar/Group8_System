from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="trainer-home"),
    path("program", views.program, name="trainer-program"),
    path("add-program", views.add_program, name="trainer-add-program"),
]