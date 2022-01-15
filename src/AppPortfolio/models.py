import os
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



def rename_img(instance, filename):
        upload_to = 'ProjectsImages/'
        ext = filename.split('.')[-1]
        if instance.slug:
            filename = f"{instance.niveau}/{instance.slug}_{instance.update_date}.{ext}"
        return os.path.join(upload_to, filename)
    
class Project(models.Model):
    
    # Champ titre du projet
    title = models.CharField(max_length=128, verbose_name='Titre')
    
    # Champ auteur du projet
    author = models.ForeignKey(User, related_name='author_username', on_delete=models.CASCADE, verbose_name='Auteur')
    
    # Champ slug du projet
    slug = models.SlugField(null=True, blank=True)
    
    # Champ Niveau du projet (débutant, intermédiaire, avancé)
    list_niveau = (
        ('debutant', 'Débutant'),
        ('intermediaire', 'Intermédiaire'),
        ('avance', 'Avancé')
    )
    niveau = models.CharField(max_length=60, choices=list_niveau, verbose_name='Niveau')
    
    # Champ date de création du projet
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='date Creation')
    
    # Champ date de modification du projet
    update_date = models.DateTimeField(auto_now=True, verbose_name='date de modification')
    
    # Champ language de programmation utliser du projet
    technology = models.CharField(max_length=500, verbose_name='Technologie')
    
    # Champ introduction du projet
    introduction = models.TextField(verbose_name='Introduction')
    
    # Champ body c'est à dire le contenu et le dédail du projet
    body = models.TextField()
    
    # Champ image du projet
    image = models.ImageField(upload_to=rename_img)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    
    
    