from csv import list_dialects
from django.contrib import admin

from AppPortfolio.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'create_date',
        'title',
        'nom_du_auteur',
        'niveau',
        'technology',
        'status',
        'published_date',
        'update_date',
    )
    
    search_fields = (
        'title',
        'author__first_name',
        'author__last_name',
    )
    
    list_filter = (
        'niveau',
        'status',
        'create_date',
        'published_date',
    )
    
    list_editable = (
        'title',
        'niveau',
        'technology',
        'status',
        'published_date',
    )
    
    def nom_du_auteur(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

admin.site.register(Project, ProjectAdmin)