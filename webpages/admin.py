from django.contrib import admin
from .models import ContactSubmission, Plan
# Register your models here.

class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')
    ordering = ('id',)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    ordering = ('id',)

# Register your models here.
admin.site.register(ContactSubmission, ContactSubmissionAdmin)
admin.site.register(Plan, PlanAdmin)