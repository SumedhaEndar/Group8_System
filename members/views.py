from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.decorators import member_required

@login_required
@member_required
# Create your views here.
def home(request):
    return render(request, 'members/member_home.html', {})
