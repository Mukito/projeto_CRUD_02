from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contatos/', include('contatos.urls')),  # Inclui as rotas do app contatos
]
