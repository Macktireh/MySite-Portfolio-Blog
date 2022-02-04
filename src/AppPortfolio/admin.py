from csv import list_dialects
from django.contrib import admin

from AppPortfolio.models import Category, Competence, Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'create_date',
        'title',
        'nom_du_auteur',
        'niveau',
        'technology',
        'favorites',
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
        'favorites',
        'status',
        'create_date',
        'published_date',
    )
    
    list_editable = (
        'title',
        'niveau',
        'technology',
        'favorites',
        'status',
    )
    
    prepopulated_fields = {'slug': ('title',)}
    
    def nom_du_auteur(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

admin.site.register(Project, ProjectAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'update_date',
        'category',
        'slug',
    )
    
    search_fields = (
        'category',
    )
    
    list_editable = (
        'category',
    )
    
    prepopulated_fields = {'slug': ('category',)}
    
admin.site.register(Category, CategoryAdmin)


class CompetenceAdmin(admin.ModelAdmin):
    list_display = (
        'update_date',
        'sort_order',
        'title',
        'description',
        'icon',
    )
    
    search_fields = (
        'title',
    )
    
    list_editable = (
        'sort_order',
        'title',
        'description',
        'icon',
    )
    
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Competence, CompetenceAdmin)