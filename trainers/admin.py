from django.contrib import admin
from .models import FitnessProgram


class FitnessProgramAdmin(admin.ModelAdmin):
    list_display = ('program_id', 'program_name', 'program_day', 'program_time', 'program_pax', 'program_price', 'trainer', 'program_images')
    ordering = ('program_id',)

# Register your models here.
admin.site.register(FitnessProgram, FitnessProgramAdmin)