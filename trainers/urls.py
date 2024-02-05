from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="trainer-home"),
    path("program", views.program, name="trainer-program"),
    path("add-program", views.add_program, name="trainer-add-program"),
    path('trainer-program-detail/<str:program_name>/', views.trainer_program_detail, name='trainer-program-detail'),
    path('delete-program/<str:program_name>/', views.delete_program, name='delete-program'),
]