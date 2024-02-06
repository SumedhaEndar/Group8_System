from django.contrib import admin
from .models import PaymentNotification

# Register your models here.
class PaymentNotificationAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'message', 'outstanding_payment')
    ordering = ('user_id',)

# Register your models here.
admin.site.register(PaymentNotification, PaymentNotificationAdmin)