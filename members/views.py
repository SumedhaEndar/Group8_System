from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.decorators import member_required
from trainers.models import FitnessProgram
from users.models import Member, Admin, Trainer, User
from .models import ProgramEnroll

@login_required
@member_required
# Create your views here.
def home(request):
    return render(request, 'members/member_home.html', {})

@login_required
@member_required
def payment_page(request, program_type, program_id):
    current_user = request.user

    model_mapping = {
        'fitness-program': FitnessProgram
    }

    model = model_mapping.get(program_type)

    if not model:
        return render(request, 'error.html', {'error_message': 'Invalid item type'})

    program = get_object_or_404(model, program_id=program_id)

    context = {
        'program': program,
        'current_user': current_user
    }
    # print(current_user)
    # print(current_user.member.full_name)
    return render(request, 'members/payment-page.html', context)


@login_required
@member_required
def make_payment(request, program_id):
    if request.method == 'POST':
        program = get_object_or_404(FitnessProgram, program_id=program_id)
        
        # Assuming you have a logged-in user (member)
        # member = request.user # Adjust this based on your actual user model

        # Create a ProgramEnroll instance
        ProgramEnroll.objects.create(program=program, member=Member.objects.get(user=request.user))
        print('Hello')

    return redirect('home') 

@login_required
@member_required
def progress(request):
    return render(request, 'members/member-progress.html', {})

@login_required
@member_required
def qrcode(request):
    return render(request, 'members/member-code.html', {})

@login_required
@member_required
def account(request):
    return render(request, 'members/member-account.html', {})