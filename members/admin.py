from django.contrib import admin
from .models import ProgramEnroll, PlanSubscribe

class ProgramEnrollAdmin(admin.ModelAdmin):
    list_display = ('id', 'member_id', 'program_id', 'left')
    ordering = ('id',)

class PlanSubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'member_id', 'plan_id', 'valid_from')
    ordering = ('id',)

# Register your models here.
admin.site.register(ProgramEnroll, ProgramEnrollAdmin)
admin.site.register(PlanSubscribe, PlanSubscribeAdmin)