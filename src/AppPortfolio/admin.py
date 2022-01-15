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
        'update_date',
        'image',
    )
    
    search_fields = (
        'title',
        'nom_du_auteur',
        'niveau',
        'technology',
    )
    
    list_editable = (
        'title',
        'niveau',
        'technology',
    )
    
    def nom_du_auteur(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

admin.site.register(Project, ProjectAdmin)