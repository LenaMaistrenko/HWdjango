from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def toyota(request):
    return render(request, 'toyota.html')


def honda(request):
    return render(request, 'honda.html')


def renault(request):
    return render(request, 'renault.html')
