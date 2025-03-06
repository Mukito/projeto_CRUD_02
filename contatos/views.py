from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from .forms import ContatoForm  # Vamos criar esse formulário já já
from django.contrib import messages

# Listar Contatos
#def lista_contatos(request):
#    contatos = Contato.objects.all()
#    return render(request, 'contatos/lista.html', {'contatos': contatos})

def lista_contatos(request):
    query = request.GET.get('q')
    if query:
        contatos = Contato.objects.filter(nome__icontains=query)
    else:
        contatos = Contato.objects.all()
    return render(request, 'contatos/lista.html', {'contatos': contatos})



# Criar Contato
def criar_contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contato adicionado com sucesso!")
            return redirect('lista_contatos')
    else:
        form = ContatoForm()
    return render(request, 'contatos/form.html', {'form': form})

# Editar Contato
def editar_contato(request, id):
    contato = get_object_or_404(Contato, id=id)
    if request.method == 'POST':
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            messages.success(request, "Contato atualizado com sucesso!")
            return redirect('lista_contatos')
    else:
        form = ContatoForm(instance=contato)
    return render(request, 'contatos/form.html', {'form': form})

# Deletar Contato
def deletar_contato(request, id):
    contato = get_object_or_404(Contato, id=id)
    contato.delete()
    messages.error(request, "Contato excluído!")
    return redirect('lista_contatos')

# 
