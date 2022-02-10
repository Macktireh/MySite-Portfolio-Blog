from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from config.settings.base import EMAIL_HOST_USER, EMAIL_LIST_RECIPIENT
from .models import Contact, Project, Competence
from .forms import ContactForm
from django.core.mail import send_mail


# view home
def home(request):
    Projects = Project.objects.filter(favorites=True)
    Competences = Competence.objects.all()
    contexte = {
        'Projects': Projects,
        'Competences': Competences
    }
    template = 'portfolio/pages/home.html'
    return render(request, template, contexte)


# view project
def project(request):
    
    Projects = Project.objects.all()
    contexte = {
        'Projects': Projects,
    }
    template = 'portfolio/pages/project.html'
    return render(request, template, contexte)


# view detail project
def detail_project(request, slug):
    project = Project.objects.get(slug=slug)
    contexte = {
        'Project': project,
    }
    template = 'portfolio/pages/detail_project.html'
    return render(request, template, contexte)


def blog(request):
    template = 'portfolio/pages/blog.html'
    return render(request, template)


# view Contact
def contact(request):
        
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            date_send = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
            
            body = f"""
MESSAGE :
{message}

FROM :
{name}
{email}

Date : 
{date_send}
            """
            send_mail(
                f'Contact depuis votre site web par : {name}',
                body,
                f'{EMAIL_HOST_USER}',
                EMAIL_LIST_RECIPIENT
            )
            
            form.save()
            return redirect('thank_you')
    
    else:
        form = ContactForm()
    contexte = {
        'forms': form    
    }
    template = 'portfolio/pages/contact.html'
    return render(request, template, contexte)


def merci(request):
    contacts = Contact.objects.all()
    contexte = {
        'contacts': contacts    
    }
    template = 'portfolio/pages/thanks.html'
    return render(request, template, contexte)