from django.contrib import admin
from .models import User, Admin, Trainer, Member

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Trainer)
admin.site.register(Member)