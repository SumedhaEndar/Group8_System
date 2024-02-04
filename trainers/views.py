from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.decorators import trainer_required
from users.models import Member, Admin, Trainer, User
from .forms import FitnessProgramForm


@login_required
@trainer_required
# Create your views here.
def home(request):
    current_user = request.user 

    # Accessing data from the current_user
    full_name = current_user.trainer.full_name
    age = current_user.trainer.age
    bmi = current_user.trainer.bmi
    bmr = current_user.trainer.bmr
    phone = current_user.trainer.phone
    email = User.objects.get(username=current_user).email
    
    return render(
        request, 
        'trainers/trainer-home.html', 
        {
            "trainer_name": full_name,
            "age": age,
            "bmi": bmi,
            "bmr": bmr,
            "phone": phone,
            "email": email,
        }
    )


@login_required
@trainer_required
def program(request):
    
    return render(
        request, 
        'trainers/trainer-program.html', 
        {}
    )


@login_required
@trainer_required
def add_program(request):
    if request.method == 'POST':
        form = FitnessProgramForm(request.POST, request.FILES)
        if form.is_valid():
            fitness_program = form.save(commit=False)
            fitness_program.trainer = Trainer.objects.get(user=request.user)
            fitness_program.save()
            return redirect('trainer-program')  # Replace 'success_url' with your desired success URL
    else:
        form = FitnessProgramForm()

    return render(
        request, 
        'trainers/trainer-add-program.html', 
        {'form':form}
    )
