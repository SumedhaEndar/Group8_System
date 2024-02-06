from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.decorators import trainer_required
from users.models import Member, Admin, Trainer, User
from trainers.models import FitnessProgram
from .forms import FitnessProgramForm, FitnessProgramEditForm
from django.contrib import messages
from django.http import HttpRequest

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
    fitness_programs = FitnessProgram.objects.all()
    return render(
        request,
        'trainers/trainer-program.html', 
        {'fitness_programs':fitness_programs}
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

@login_required
@trainer_required
def edit_time(request, program_name):
    program = get_object_or_404(FitnessProgram, program_name=program_name)

    if request.method == 'POST':
        form = FitnessProgramEditForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('trainer-timetable')
    else:
        form = FitnessProgramEditForm(instance=program)

    return render(request, 'trainers/trainer-edit-time.html', {'form': form, 'program': program})

@login_required
@trainer_required
def trainer_program_detail(request, program_name):
    program = get_object_or_404(FitnessProgram, program_name=program_name)
    return render(request, 'trainers/trainer-program-detail.html', {'program': program})

@login_required
@trainer_required
def delete_program(request, program_name):
    program = get_object_or_404(FitnessProgram, program_name=program_name)
    
    if request.method == 'POST':
        # Delete the program
        program.delete()
        messages.success(request, f'The program "{program_name}" has been deleted.')
        return redirect('trainer-program')

    return redirect('trainers/trainer-program-detail.html', program_name=program_name)

@login_required
@trainer_required
def trainer_timetable(request):
    
    TIME = (
        ('08:00 - 09:00', '8:00 am - 9:00 am'),
        ('09:00 - 10:00', '9:00 am - 10:00 am'),
        ('10:00 - 11:00', '10:00 am - 11:00 am'),
        ('18:00 - 19:00', '6:00 pm - 7:00 pm'),
        ('19:00 - 20:00', '7:00 pm - 8:00 pm'),
        ('20:00 - 21:00', '8:00 pm - 9:00 pm'),
    )
    timetable_data = []

    for time_slot, time_label in TIME:
        programs = FitnessProgram.objects.filter(program_time=time_slot).order_by('program_day')
        timetable_data.append({'time_slot': time_slot, 'time_label': time_label, 'programs': programs})

    return render(request, 'trainers/trainer-timetable.html', {'timetable_data': timetable_data})

# def trainer_timetable(request):
#     days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     timetable_data = []

#     for day in days_of_week:
#         programs = FitnessProgram.objects.filter(program_day=day).order_by('program_time')
#         timetable_data.append({'day': day, 'programs': programs})

#     return render(request, 'trainers/trainer-timetable.html', {'timetable_data': timetable_data})

@login_required
@trainer_required
def trainer_program_detail(request, program_name):
    program = get_object_or_404(FitnessProgram, program_name=program_name)
    return render(request, 'trainers/trainer-program-detail.html', {'program': program})

@login_required
@trainer_required
def delete_program(request, program_name):
    program = get_object_or_404(FitnessProgram, program_name=program_name)
    
    if request.method == 'POST':
        # Delete the program
        program.delete()
        messages.success(request, f'The program "{program_name}" has been deleted.')
        return redirect('trainer-program')

    return redirect('trainers/trainer_programDetail', program_name=program_name)