from django.contrib import admin
from .models import User, Admin, Trainer, Member

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_superuser', 'is_admin', 'is_trainer', 'is_member', 'is_active')
    ordering = ('id',)

class AdminAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user',  'full_name', 'created_at')
    ordering = ('user_id',)

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'full_name', 'phone', 'trainer_certificate', 'age', 'bmi', 'bmr', 'created_at')
    ordering = ('user_id',)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'full_name', 'phone', 'created_at')
    ordering = ('user_id',)


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Member, MemberAdmin)