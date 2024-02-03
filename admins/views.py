from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.decorators import admin_required
from users.models import Member, Admin, Trainer, User

@login_required
@admin_required
# Create your views here.
def home(request):
    current_user = request.user 
    # Accessing data from the current_user
    full_name = current_user.admin.full_name
    email = User.objects.get(username=current_user).email

    return render(
        request, 
        'admins/admin-home.html', 
        {
            'admin_name':full_name,
            'admin_email':email
        }
    )