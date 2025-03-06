# Projeto_IA_CRUD
Treinamento CRUD completo
![image](https://github.com/user-attachments/assets/6b89424d-ade9-4801-a766-c184b45c2ded)


# Projeto_IA_CRUD
Treinamento CRUD completo
**Inicio**<br>
`django-admin startproject projeto .`<br>
`python manage.py startapp contatos`<br>
## 1️⃣ Adicionar o app ao Django
Abra o arquivo projeto/settings.py e adicione 'contatos' na lista de INSTALLED_APPS:
## 2️⃣ Criar o modelo (Model) do banco de dados
Abra o arquivo **contatos/models.py** e defina a estrutura da tabela:

```
from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
```
## 3️⃣ Criar as tabelas no banco de dados
Após definir o modelo, rode estes comandos para aplicar as migrações:
```
python manage.py makemigrations
python manage.py migrate

```
## 4️⃣ Criar as Views (Lógica do CRUD)
Abra o arquivo contatos/views.py e adicione as funções para listar, criar, editar e deletar contatos:
```
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from .forms import ContatoForm  # Vamos criar esse formulário já já

# Listar Contatos
def lista_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/lista.html', {'contatos': contatos})

# Criar Contato
def criar_contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
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
            return redirect('lista_contatos')
    else:
        form = ContatoForm(instance=contato)
    return render(request, 'contatos/form.html', {'form': form})

# Deletar Contato
def deletar_contato(request, id):
    contato = get_object_or_404(Contato, id=id)
    contato.delete()
    return redirect('lista_contatos')

```
## 5️⃣ Criar o Formulário
Para facilitar o envio de dados, crie um arquivo chamado contatos/forms.py e adicione o seguinte código:
```
from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone']

```

## 6️⃣ Criar as URLs do App
Crie um arquivo contatos/urls.py e adicione as rotas:
```
from django.urls import path
from .views import lista_contatos, criar_contato, editar_contato, deletar_contato

urlpatterns = [
    path('', lista_contatos, name='lista_contatos'),
    path('novo/', criar_contato, name='criar_contato'),
    path('editar/<int:id>/', editar_contato, name='editar_contato'),
    path('deletar/<int:id>/', deletar_contato, name='deletar_contato'),
]
```
Agora, precisamos registrar essas URLs no projeto.
Abra projeto/urls.py e adicione esta linha:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contatos/', include('contatos.urls')),  # Inclui as rotas do app contatos
]

```
## 7️⃣ Criar os Templates
Agora precisamos criar os arquivos HTML para exibir os contatos.
Dentro da pasta contatos/templates/contatos/, crie os seguintes arquivos:

📄 lista.html (Página que lista os contatos)
```
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Lista de Contatos</title>
</head>
<body>
    <h1>Lista de Contatos</h1>
    <a href="{% url 'criar_contato' %}">Adicionar Contato</a>
    <ul>
        {% for contato in contatos %}
            <li>
                {{ contato.nome }} - {{ contato.email }} - {{ contato.telefone }}
                <a href="{% url 'editar_contato' contato.id %}">Editar</a>
                <a href="{% url 'deletar_contato' contato.id %}">Deletar</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```
📄 form.html (Página de criação e edição de contatos)
```
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Contato</title>
</head>
<body>
    <h1>Adicionar/Editar Contato</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Salvar</button>
    </form>
    <a href="{% url 'lista_contatos' %}">Voltar</a>
</body>
</html>

```
## 8️⃣ Testar no Navegador
Agora execute o servidor Django:
```
python manage.py runserver
```
## =========================

## 1️⃣ Adicionar Bootstrap ao Projeto
Para estilizar o CRUD, vamos usar o Bootstrap 5. Edite seus templates e adicione este link no <head>:
```
<head>
    <meta charset="UTF-8">
    <title>Lista de Contatos</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
```
## 2️⃣ Melhorando lista.html
Abra lista.html e substitua pelo código abaixo para deixar a página mais bonita:
```
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Lista de Contatos</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container mt-4">
    <h1 class="text-center">Lista de Contatos</h1>
    
    <a href="{% url 'criar_contato' %}" class="btn btn-success mb-3">Adicionar Contato</a>

    <table class="table table-bordered">
        <thead class="table-dark">
            <tr>
                <th>Nome</th>
                <th>Email</th>
                <th>Telefone</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            {% for contato in contatos %}
                <tr>
                    <td>{{ contato.nome }}</td>
                    <td>{{ contato.email }}</td>
                    <td>{{ contato.telefone }}</td>
                    <td>
                        <a href="{% url 'editar_contato' contato.id %}" class="btn btn-warning btn-sm">Editar</a>
                        <a href="{% url 'deletar_contato' contato.id %}" class="btn btn-danger btn-sm">Deletar</a>
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>

```
## 📄 3️⃣ Melhorando form.html
Agora vamos deixar o formulário mais bonito:
```
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Contato</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container mt-4">
    <h1 class="text-center">Adicionar/Editar Contato</h1>

    <div class="card p-4">
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit" class="btn btn-primary">Salvar</button>
            <a href="{% url 'lista_contatos' %}" class="btn btn-secondary">Voltar</a>
        </form>
    </div>
</body>
</html>

```
## 4️⃣ Adicionar Mensagens de Sucesso/Erro
Vamos melhorar a experiência do usuário adicionando mensagens quando um contato for criado, editado ou excluído.

🔹 Modificar as Views no views.py
Abra contatos/views.py e importe messages no início do arquivo:
```
from django.contrib import messages
```
Agora, modifique as funções para incluir mensagens:
```
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
```
## Mostrar mensagens no lista.html
Agora, antes da <table>, adicione isso para exibir as mensagens:
```
{% if messages %}
    <div class="alert alert-dismissible fade show">
        {% for message in messages %}
            <div class="alert {% if message.tags == 'success' %}alert-success{% elif message.tags == 'error' %}alert-danger{% endif %}">
                {{ message }}
            </div>
        {% endfor %}
    </div>
{% endif %}

```
## 5️⃣ Adicionar Barra de Pesquisa
Agora vamos permitir que o usuário pesquise contatos pelo nome!

🔹 Modificar a View lista_contatos
Abra views.py e modifique a função de listagem:
```
def lista_contatos(request):
    query = request.GET.get('q')
    if query:
        contatos = Contato.objects.filter(nome__icontains=query)
    else:
        contatos = Contato.objects.all()
    return render(request, 'contatos/lista.html', {'contatos': contatos})
```

## 🔹 Adicionar a Barra de Pesquisa em lista.html
Antes da <table>, adicione um formulário de busca:
```
<form method="GET" class="mb-3">
    <input type="text" name="q" class="form-control" placeholder="Buscar por nome...">
    <button type="submit" class="btn btn-primary mt-2">Buscar</button>
</form>

```
** Ideias de evolução **

✅ Página de confirmação antes de excluir contatos.<br>
✅ Autenticação (login/logout) para proteger o sistema.<br>
✅ Paginação para não mostrar todos os contatos de uma vez.<br>
✅ Exportar contatos para CSV ou PDF.<br>
✅ API REST com Django REST Framework (para integrar com apps ou outras plataformas).<br>
