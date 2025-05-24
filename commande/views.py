from django.shortcuts import render, redirect
from .models import Produit, Client
from .forms import ProduitForm, ClientForm

def liste_produits(request):
    produits = Produit.objects.all()  # ✅ 'produits' est une variable
    return render(request, 'liste_produits.html', {'produits': produits})

def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'liste_clients.html', {'clients': clients})


def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')  # redirige vers la liste des produits
    else:
        form = ProduitForm()
    return render(request, 'commande/ajouter_produit.html', {'form': form})

def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')  # redirige vers la liste des clients
    else:
        form = ClientForm()
    return render(request, 'commande/ajouter_client.html', {'form': form})
