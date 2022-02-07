from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project, name='projects'),
    path('projects/<slug:slug>', views.detail_project, name='detail_project'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('tkank-you-for-your-message/', views.merci, name='thank_you'),
]