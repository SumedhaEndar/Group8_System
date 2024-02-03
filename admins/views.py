from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.decorators import admin_required

@login_required
@admin_required
# Create your views here.
def home(request):
    return render(request, 'admins/admin_home.html', {})