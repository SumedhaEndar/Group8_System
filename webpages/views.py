from django.shortcuts import render, get_object_or_404, redirect
from trainers.models import FitnessProgram
from .forms import ContactForm
from .models import ContactSubmission
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            ContactSubmission.objects.create(name=name, email=email, message=message)
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'webpages/contactUs.html', {'form': form})
