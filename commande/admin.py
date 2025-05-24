from django.contrib import admin
from .models import Produit, Client

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'stock')

admin.site.register(Produit, ProduitAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'telephone')

admin.site.register(Client, ClientAdmin)





