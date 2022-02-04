from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project, name='project'),
    path('projects/<slug:slug>', views.detail_project, name='detail_project'),
]