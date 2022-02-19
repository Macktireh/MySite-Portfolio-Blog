import os
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField


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
    title = models.CharField(max_length=128, verbose_name='Titre')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Auteur')
    slug = models.SlugField(null=True, blank=True, unique=True)
    
    list_niveau = (
        ('Débutant', 'Débutant'),
        ('Intermédiaire', 'Intermédiaire'),
        ('Avancé', 'Avancé')
    )
    niveau = models.CharField(max_length=60, choices=list_niveau, verbose_name='Niveau')
    technology = models.CharField(max_length=500, verbose_name='Technologie')
    introduction = models.TextField(verbose_name='Introduction')
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to=rename_img)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Date Creation')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
    
    STATUS_CHOICES = (
        ('draft', 'Brouillon'),
        ('published', 'Publié')
    )
    status = models.CharField(choices=STATUS_CHOICES, default="draft", max_length=20)
    published_date = models.DateTimeField(default=timezone.now(), verbose_name='Date de Publication')
    favorites = models.BooleanField(default=False)
    number_views = models.IntegerField(_('Number of Views'), default=0, blank=True, null=True)
    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    
    
class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Catégorie')
    slug = models.SlugField(max_length=100, unique=True)
    update_date = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    
    def __str__(self):
        return self.category
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super().save(*args, **kwargs)


class Competence(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)
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
    name = models.CharField(verbose_name='Name', max_length=50)
    email = models.EmailField(verbose_name='Adress Email', unique=True)
    subject = models.CharField(verbose_name='Subject', max_length=128, blank=True, null=True)
    message = models.TextField(verbose_name='Message', max_length=10000)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.name