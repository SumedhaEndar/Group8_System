from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.decorators import trainer_required

@login_required
@trainer_required
# Create your views here.
def home(request):
    return render(request, 'trainers/trainer_home.html', {})