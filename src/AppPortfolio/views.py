from django.shortcuts import render
from .models import Project


def home(request):
    
    # récuperer toutes les données depuis la base de données
    Projects = Project.objects.filter(favorites=True)
    
    # contexte : passer les données au gabarite de django
    contexte = {
        'Projects': Projects,
    }
    
    # le schema du document à rendre ou afficher 
    template = 'AppPortfolio/home.html'
    
    return render(request, template, contexte)


def project(request):
    
    # récuperer toutes les données depuis la base de données
    Projects = Project.objects.all()
    
    # contexte : passer les données au gabarite de django
    contexte = {
        'Projects': Projects,
    }
    
    # le schema du document à rendre ou afficher 
    template = 'AppPortfolio/project.html'
    
    return render(request, template, contexte)