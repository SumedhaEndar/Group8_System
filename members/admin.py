from django.contrib import admin
from .models import ProgramEnroll

class ProgramEnrollAdmin(admin.ModelAdmin):
    list_display = ('id', 'member_id', 'program_id')
    ordering = ('id',)

# Register your models here.
admin.site.register(ProgramEnroll, ProgramEnrollAdmin)