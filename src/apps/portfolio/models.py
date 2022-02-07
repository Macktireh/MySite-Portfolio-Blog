import os
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _



def rename_img(instance, filename):
    upload_to = 'image_projet'
    ext = filename.split('.')[-1]
    if instance.slug:
        if ext in ['jpg', 'jpeg', 'JPG', 'JPEG']:
            filename = f"jpg/{instance.slug}_{instance.update_date}.{ext}"
        elif ext in ['png', 'PNG']:
            filename = f"png/{instance.slug}_{instance.update_date}.{ext}"
        else:
            filename = f"auther/{instance.slug}_{instance.update_date}.{ext}"
    return os.path.join(upload_to, filename)

def rename_file(instance, filename):
    upload_to = 'image_competence'
    ext = filename.split('.')[-1]
    if instance.slug:
        if ext in ['jpg', 'jpeg', 'JPG', 'JPEG']:
            filename = f"jpg/{instance.slug}_{instance.update_date}.{ext}"
        elif ext in ['png', 'PNG']:
            filename = f"png/{instance.slug}_{instance.update_date}.{ext}"
        elif ext in ['svg', 'SVG']:
            filename = f"svg/{instance.slug}_{instance.update_date}.{ext}"
        else:
            filename = f"auther/{instance.slug}_{instance.update_date}.{ext}"
    return os.path.join(upload_to, filename)
    
class Project(models.Model):
    
    # Champ titre du projet
    title = models.CharField(max_length=128, verbose_name='Titre')
    
    # Champ auteur du projet
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Auteur')
    
    # Champ slug du projet
    slug = models.SlugField(null=True, blank=True)
    
    # Champ Niveau du projet (débutant, intermédiaire, avancé)
    list_niveau = (
        ('Débutant', 'Débutant'),
        ('Intermédiaire', 'Intermédiaire'),
        ('Avancé', 'Avancé')
    )
    niveau = models.CharField(max_length=60, choices=list_niveau, verbose_name='Niveau')
    
    # Champ date de création du projet
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Date Creation')
    
    # Champ date de modification du projet
    update_date = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
    
    # Champ language de programmation utliser du projet
    technology = models.CharField(max_length=500, verbose_name='Technologie')
    
    # Champ introduction du projet
    introduction = models.TextField(verbose_name='Introduction')
    
    # Champ body c'est à dire le contenu et le dédail du projet
    body = models.TextField(blank=True)
    
    # Champ image du projet
    image = models.ImageField(upload_to=rename_img)
    
    # Champ status du projet
    STATUS_CHOICES = (
        ('draft', 'Brouillon'),
        ('published', 'Publié')
    )
    status = models.CharField(choices=STATUS_CHOICES, default="draft", max_length=20)
    
    # Champ date de publication du projet
    published_date = models.DateTimeField(default=timezone.now(), verbose_name='Date de Publication')
    
    # Projet favorie
    favorites = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    
    
class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Catégorie')
    slug = models.SlugField(max_length=100)
    update_date = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    
    def __str__(self):
        return self.category
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super().save(*args, **kwargs)


class Competence(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    description = models.CharField(_('Description'), max_length=128, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
    icon = models.FileField(_('Icon'), upload_to=rename_file, blank=True, null=True)
    sort_order = models.IntegerField(_('Sort'), unique=True, blank=True, null=True)
    
    class Meta:
        ordering = ['sort_order']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
        
class Contact(models.Model):
    name = models.CharField(verbose_name='Name', max_length=30)
    email = models.EmailField(verbose_name='Adress Email', unique=True)
    # date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    message = models.TextField(verbose_name='Message', max_length=5000)
    
    # class Meta:
    #     ordering = ['-date']
    
    def __str__(self):
        return self.name