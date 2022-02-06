from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project, name='projects'),
    path('projects/<slug:slug>', views.detail_project, name='detail_project'),
    path('contact/', views.contact, name='contact'),
]