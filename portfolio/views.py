from django.shortcuts import render
from .models import Projet


def home(request):
    projects = Projet.objects.all()
    return render(request, 'home.html', {'projects': projects})


