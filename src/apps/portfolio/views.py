from django.shortcuts import render
from .models import Project, Competence

# view home
def home(request):
    
    # récuperer toutes les données depuis la base de données
    Projects = Project.objects.filter(favorites=True)
    Competences = Competence.objects.all()
    
    # contexte : passer les données au gabarite de django
    contexte = {
        'Projects': Projects,
        'Competences': Competences
    }
    
    # le schema du document à rendre ou afficher 
    template = 'portfolio/pages/home.html'
    
    return render(request, template, contexte)


# view project
def project(request):
    
    # récuperer toutes les données depuis la base de données
    Projects = Project.objects.all()
    
    # contexte : passer les données au gabarite de django
    contexte = {
        'Projects': Projects,
    }
    
    # le schema du document à rendre ou afficher 
    template = 'portfolio/pages/project.html'
    
    return render(request, template, contexte)


# view detail project
def detail_project(request, slug):
    
    # récuperer toutes les données depuis la base de données
    project = Project.objects.get(slug=slug)
    
    # contexte : passer les données au gabarite de django
    contexte = {
        'Project': project,
    }
    
    # le schema du document à rendre ou afficher 
    template = 'portfolio/pages/detail_project.html'
    
    return render(request, template, contexte)


# view Contact
def contact(request):
    
    # contexte : passer les données au gabarite de django
    contexte = {

    }
    
    # le schema du document à rendre ou afficher 
    template = 'portfolio/pages/contact.html'
    
    return render(request, template, contexte)