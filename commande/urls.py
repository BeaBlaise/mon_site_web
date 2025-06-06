from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import register, inscription


urlpatterns = [
    path('produits/', views.liste_produits, name='liste_produits'),
    path('clients/', views.liste_clients, name='liste_clients'),
    path('produits/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('clients/ajouter/', views.ajouter_client, name='ajouter_client'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('inscription/', inscription, name='inscription'),
]


