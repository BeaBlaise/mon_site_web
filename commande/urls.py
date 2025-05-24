from django.urls import path
from .views import liste_produits, liste_clients, ajouter_produit, ajouter_client

urlpatterns = [
    path('produits/', liste_produits, name='liste_produits'),
    path('clients/', liste_clients, name='liste_clients'),
    path('produits/ajouter/', ajouter_produit, name='ajouter_produit'),
    path('clients/ajouter/', ajouter_client, name='ajouter_client'),
]
