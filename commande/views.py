from django.shortcuts import render, redirect
from .models import Produit, Client
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .formebea import ProduitForm, ClientForm, InscriptionForm
# ✅ Inscription d’un nouvel utilisateur

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = InscriptionForm()
    return render(request, 'inscription.html', {'form': form})

# ✅ Tableau de bord
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# ✅ Liste des produits
@login_required
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'liste_produits.html', {'produits': produits})

# ✅ Liste des clients
@login_required
def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'liste_clients.html', {'clients': clients})

# ✅ Ajouter un produit
@login_required
def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'commande/ajouter_produit.html', {'form': form})

# ✅ Ajouter un client
@login_required
def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')
    else:
        form = ClientForm()
    return render(request, 'commande/ajouter_client.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = InscriptionForm()
    return render(request, 'inscription.html', {'form': form})