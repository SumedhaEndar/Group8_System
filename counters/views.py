from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.decorators import counter_required
from users.models import Member, User, Counter
from members.models import ProgramEnroll, PlanSubscribe
from datetime import datetime, timedelta

# Create your views here.

@login_required
@counter_required
def home(request):
    query = request.GET.get('username', '')
    members = []

    if query:
        members = Member.objects.filter(user__username__icontains=query)

        # Fetching the enrolled programs for each member
        for member in members:
            program_enrollments = ProgramEnroll.objects.filter(member=member)
            member.program_enrollments = [{'program': enrollment.program, 'left': enrollment.left} for enrollment in program_enrollments]

            plan_subscriptions = PlanSubscribe.objects.filter(member=member)
            member.plan_subscriptions = [{'plan': subscription.plan, 'valid_from': subscription.valid_from} for subscription in plan_subscriptions]

            # Perform date calculation for plan subscription
            for subscription in member.plan_subscriptions:

                if(str(subscription['plan'])=="Yearly"):
                    subscription['valid_until'] = subscription['valid_from'] + timedelta(days=365)  

                elif(str(subscription['plan'])=="Monthly"):
                    subscription['valid_until'] = subscription['valid_from'] + timedelta(days=30)  
    
    return render(request, 'counters/counter-home.html', {'members': members, 'query': query})