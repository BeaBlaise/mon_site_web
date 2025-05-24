from django.contrib import admin
from django.urls import path, include  # ← include est important

urlpatterns = [
    path('admin/', admin.site.urls),
    path('commande/', include('commande.urls')),  # ← ceci est essentiel
]

