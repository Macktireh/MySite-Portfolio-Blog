from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Contact, Project, Competence
from .forms import ContactForm

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
    
    # contacts = Contact.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # adress_email = form.cleaned_data['adress_email']
            # message = form.cleaned_data['message']
            # p = Contact(name=name,
            #             adress_email=adress_email,
            #             message=message
            #         )
            # p.save()
            return redirect('thank_you')
    
    else:
        form = ContactForm()
    # contexte : passer les données au gabarite de django
    contexte = {
        'forms': form    
    }
    
    # le schema du document à rendre ou afficher 
    template = 'portfolio/pages/contact.html'
    
    return render(request, template, contexte)


def merci(request):
    
    contacts = Contact.objects.all()
    
    contexte = {
        'contacts': contacts    
    }
    
    # le schema du document à rendre ou afficher 
    template = 'portfolio/pages/thanks.html'
    
    return render(request, template, contexte)