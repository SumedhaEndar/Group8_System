from django.shortcuts import render, redirect
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

def managemember(request):
    # Retrieve all records from the Member table
    member_data = Member.objects.all()
    member_datas = [(member, member.user.email) for member in member_data]
    return render(
        request,
        'admins/managemember.html',
        {
            'member_datas': member_datas,
        }
    )

def edit_member(request):
    if request.method == 'POST':
        member_user = request.POST.get('member_id')
        member_full_name = request.POST.get('member_name')
        member_phone = request.POST.get('member_phone')
        member_email = request.POST.get('member_email')

        user = User.objects.get(username=member_user)
        member = Member.objects.get(user=user)
        
        # Update member details
        member.full_name = member_full_name
        member.phone = member_phone
        
        user.email = member_email  # Access the associated user and update its email
        user.save()

        member.save()

        # Redirect to the member management page
        return redirect('managemember')

def remove_member(request):
    if request.method == 'POST':
        member_user = request.POST.get('remove_member_id')

        user = User.objects.get(username=member_user)
        member = Member.objects.get(user=user)
        
        user.delete()
        member.delete()

        # Redirect to a success page or a member management page
        return redirect('managemember')

def managetrainer(request):
    # Retrieve only active trainers
    active_trainer_users = User.objects.filter(is_active=True, is_trainer=True)

    trainer_data = Trainer.objects.filter(user__in=active_trainer_users)

    trainer_datas = [(trainer, trainer.user.email) for trainer in trainer_data]

    return render(
        request,
        'admins/managetrainer.html',
        {
            'trainer_datas': trainer_datas,
        }
    )

def edit_trainer(request):
    if request.method == 'POST':
        trainer_user = request.POST.get('trainer_id')
        trainer_name = request.POST.get('trainer_name')
        trainer_age = request.POST.get('trainer_age')
        trainer_phone = request.POST.get('trainer_phone')
        trainer_email = request.POST.get('trainer_email')
        trainer_bmi = request.POST.get('trainer_bmi')
        trainer_bmr = request.POST.get('trainer_bmr')
        
        user = User.objects.get(username=trainer_user)
        trainer = Trainer.objects.get(user=user)

        # Update trainer details
        trainer.full_name = trainer_name
        trainer.age = trainer_age
        trainer.phone = trainer_phone
        trainer.bmi = trainer_bmi
        trainer.bmr = trainer_bmr

        user.email = trainer_email
        user.save()

        trainer.save()
        
        return redirect('managetrainer')  # Redirect to the trainer management page
    
def remove_trainer(request):
    if request.method == 'POST':
        trainer_user = request.POST.get('remove_trainer_id')
        
        user = User.objects.get(username=trainer_user)
        trainer = Trainer.objects.get(user=user)

        user.delete()
        trainer.delete()

        # Redirect to a success page or a trainer management page
        return redirect('managetrainer')

def trainerapplication(request):
    # Retrieve only inactive trainers
    inactive_trainer_users = User.objects.filter(is_active=False, is_trainer=True)
    trainer_data = Trainer.objects.filter(user__in=inactive_trainer_users)

    trainer_datas = [(trainer, trainer.user.email) for trainer in trainer_data]

    return render(
        request,
        'admins/trainerapplication.html',
        {
            'trainer_datas': trainer_datas,
        }
    )

def approve_trainer_application(request):
    if request.method == 'POST':
        # Retrieve the form data
        application_trainer_user = request.POST.get('applcation_trainer_id')

        user = User.objects.get(username=application_trainer_user)
        
        user.is_active = True
        user.save()

        return redirect('trainerapplication')  # Redirect to the manage trainer page after approval

def reject_trainer_application(request):
    if request.method == 'POST':
        
        # Retrieve the form data
        application_trainer_user = request.POST.get('reject_applcation_trainer_id')
    
        user = User.objects.get(username=application_trainer_user)
        trainer = Trainer.objects.get(user=user)

        user.delete()
        trainer.delete()

        # Redirect to a success page or a trainer management page
        return redirect('trainerapplication')

def outstandingpayment(request):
    # Retrieve all records from the Member table
    member_data = Member.objects.all()
    member_datas = [(member, member.user.email) for member in member_data]
    return render(
        request,
        'admins/outstandingpayment.html',
        {
            'member_datas': member_datas,
        }
    )

def paymentnotification(request):
    if request.method == 'GET':
        # Retrieve the form data
        member_user = request.GET.get('member_user')

        user = User.objects.get(username=member_user)
        member = Member.objects.get(user=user)

        return render(
            request,
            'admins/paymentnotification.html',
            {
                'member': member,
                'user': user,
            }
        )
    
# def sendpaymentnotification(request):
#     if request.method == 'POST':
#         # Retrieve the member data
#         member_id = request.POST.get('member_id')
#         member = Member.objects.get(id=member_id)

#         # Retrieve the notification message from the form
#         notification_message = request.POST.get('notification_message')

#         # Send email
#         send_mail(
#             'Payment Notification',  # Subject
#             notification_message,   # Message
#             settings.EMAIL_HOST_USER,  # Sender's email address
#             [member.email],  # Recipient's email address
#             fail_silently=False,  # Raise an exception if email sending fails
#         )

#         messages.success(request, 'Payment notification sent successfully!')

#         # Redirect to a success page or the same page
#         return redirect('outstandingpayment')