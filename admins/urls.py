from django.urls import path
from . import views

urlpatterns = [
    path("admin-home", views.home, name="admin-home"),
    path("managemember", views.managemember, name='managemember'),
    path('edit_member', views.edit_member, name='edit_member'),
    path('remove_member', views.remove_member, name='remove_member'),
    path("managetrainer", views.managetrainer, name='managetrainer'),
    path('edit_trainer', views.edit_trainer, name='edit_trainer'),
    path('remove_trainer', views.remove_trainer, name='remove_trainer'),
    path('trainerapplication', views.trainerapplication, name='trainerapplication'),
    path('approve_trainer_application', views.approve_trainer_application, name='approve_trainer_application'),
    path('reject_trainer_application', views.reject_trainer_application, name='reject_trainer_application'),
    path('outstandingpayment', views.outstandingpayment, name='outstandingpayment'),
    path('paymentnotification', views.paymentnotification, name='paymentnotification'),
    path('send_payment_notification', views.sendpaymentnotification, name='send_payment_notification'),
]