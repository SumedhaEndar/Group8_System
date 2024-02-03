from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'webpages/home.html', {})

def plans(request):
    return render(request, 'webpages/plans.html', {})

def programs(request):
    return render(request, 'webpages/programs.html', {})

def fitnessLocator(request):
    return render(request, 'webpages/fitnessLocator.html', {})

def contactUs(request):
    return render(request, 'webpages/contactUs.html', {})
