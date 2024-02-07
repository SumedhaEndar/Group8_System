from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.decorators import member_required
from trainers.models import FitnessProgram
from users.models import Member, Admin, Trainer, User
from .models import ProgramEnroll, PlanSubscribe
from webpages.models import Plan

@login_required
@member_required
def home(request):
    
    member = request.user.member  
    member.plan_subscriptions = PlanSubscribe.objects.filter(member=member) 
    member.program_enrollments = ProgramEnroll.objects.filter(member=member) 
    return render(request, 'members/member_home.html', {'member': member})

@login_required
@member_required
def payment_page(request, program_type, program_id):
    current_user = request.user

    model_mapping = {
        'fitness-program': FitnessProgram,
        'subscription-plan': Plan
    }

    model = model_mapping.get(program_type)

    if not model:
        return render(request, 'error.html', {'error_message': 'Invalid item type'})

    program = get_object_or_404(model, pk=program_id)

    context = {
        'program': program,
        'current_user': current_user
    }

    return render(request, 'members/payment-page.html', context)


@login_required
@member_required
def make_payment(request, program_type, program_id):
    if request.method == 'POST':
        model_mapping = {
           'fitness-program': (FitnessProgram, ProgramEnroll),
            'subscription-plan': (Plan, PlanSubscribe)
        }
        model, subscription_model = model_mapping.get(program_type)
        
        if not model:
            return render(request, 'error.html', {'error_message': 'Invalid item type'})
        
        program = get_object_or_404(model, pk=program_id)
        
        # Assuming you have a logged-in user (member)
        #member = request.user # Adjust this based on your actual user model
        print(program_id)
        # Create a ProgramEnroll instance
        if program_type == 'fitness-program':
            subscription_model.objects.create(program=program, member=Member.objects.get(user=request.user))
        elif program_type == 'subscription-plan':
            subscription_model.objects.create(plan=program, member=Member.objects.get(user=request.user))

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