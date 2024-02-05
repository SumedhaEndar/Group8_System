from django.db import models
from users.models import Member

# Create your models here.
class PaymentNotification(models.Model):
    user = models.OneToOneField(Member, on_delete=models.CASCADE, primary_key=True, related_name='member')
    message = models.CharField(default=None, max_length=255)
    outstanding_payment = models.DecimalField(default=0, max_digits=10, decimal_places=2)