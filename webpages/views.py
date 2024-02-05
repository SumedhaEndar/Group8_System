from django.shortcuts import render, get_object_or_404
from trainers.models import FitnessProgram

# Create your views here.

def home(request):
    return render(request, 'webpages/home.html', {})

def programs(request):
    programs = FitnessProgram.objects.all()
    return render(request, 'webpages/programs.html', {"programs":programs})

def program_detail(request, program_id):
    program = get_object_or_404(FitnessProgram, program_id=program_id)
    return render(request, 'webpages/program-detail.html', {'program':program})

def plans(request):
    return render(request, 'webpages/plans.html', {})

def fitnessLocator(request):
    return render(request, 'webpages/fitnessLocator.html', {})

def contactUs(request):
    return render(request, 'webpages/contactUs.html', {})
