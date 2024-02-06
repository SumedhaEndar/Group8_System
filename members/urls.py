from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="member-home"),
    path("payment-page/<str:program_type>/<int:program_id>", views.payment_page, name="payment-page"),
    path("make-payment/<int:program_id>", views.make_payment, name="make-payment"),
    path("progress", views.progress, name="member-progress"),
    path("qrcode", views.qrcode, name="member-qrcode"),
    path("account", views.account, name="member-account"),
]