from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.decorators import member_required
from trainers.models import FitnessProgram
from users.models import Member, Admin, Trainer, User
from .models import ProgramEnroll, PlanSubscribe
from webpages.models import Plan
from .forms import MemberUpdateForm, PasswordUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash

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
    member_username = request.user.username
    return render(request, 'members/member-code.html', {"member_username": member_username})

@login_required
@member_required
def account(request):
    member = request.user.member  # Retrieve the member object associated with the current user
    profile_form = MemberUpdateForm(instance=member)
    if request.method == 'POST':
        if 'update_profile' in request.POST:
            profile_form = MemberUpdateForm(request.POST, instance=member)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile updated successful')
                return redirect('member-account')  # Redirect to a view that displays member details
        elif 'update_password' in request.POST:
            password_form = PasswordUpdateForm(request.POST)
            if password_form.is_valid():
                c_password = password_form.cleaned_data['current_password']
                new_password = password_form.cleaned_data['new_password']
                r_new_password = password_form.cleaned_data['retype_new_password']
                user = authenticate(username=request.user.username, password=c_password)
                if user is not None:
                    if new_password == r_new_password:
                        user.set_password(new_password)
                        user.save()
                        update_session_auth_hash(request, user)  # Important to keep the user logged in
                        messages.success(request, 'Password updated successfully')
                        return redirect('member-account')
                    else:
                        messages.error(request, 'Passwords do not match.')
                else:
                    messages.error(request, 'Incorrect current password.')
            else:
                messages.error(request, 'Password update failed. Please correct the errors.')
    else:
        profile_form = MemberUpdateForm(instance=member)
        password_form = PasswordUpdateForm()
    return render(request, 'members/member-account.html', {'profile_form': profile_form, 'password_form': password_form})