from django.urls import path
from .views import lista_contatos, criar_contato, editar_contato, deletar_contato

urlpatterns = [
    path('', lista_contatos, name='lista_contatos'),
    path('novo/', criar_contato, name='criar_contato'),
    path('editar/<int:id>/', editar_contato, name='editar_contato'),
    path('deletar/<int:id>/', deletar_contato, name='deletar_contato'),
]
