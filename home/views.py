from django.contrib.messages.context_processors import messages
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, Http404, get_object_or_404
from django.contrib.auth.decorators import login_required
from medico.models import cadastro_medicos
from django.http import HttpResponseRedirect


def index_home(request):
    return HttpResponseRedirect('buscar')


def mostrar(request, idbusca):
    dados = get_object_or_404(cadastro_medicos, id=idbusca)
    return render(request, 'home/detMedico.html', {'dados': dados})


def buscar(request):
    x = ''
    dados = cadastro_medicos.objects.all()

    try:
        x = request.GET['buscar']
        dados = cadastro_medicos.objects.order_by('nome').filter(
            Q(nome__icontains=x) | Q(especialidade__icontains=x)
        )
        if x is None or not x:
            messages.add_message(request, messages.INFO, 'Digite um valor válido')
            return render(request, 'home/index.html')
    except:
        dados = cadastro_medicos.objects.all()



    return render(request, 'home/index.html', {'dados': dados})


def opcao(request):
    return render(request, 'home/opcao.html')


def cadastrar(request):
    if request.method != 'POST':
        return render(request, 'home/cadastro.html')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    nome = request.POST.get('nome')
    tipo = request.POST.get('tipo')
    senha1 = request.POST.get('senha1')

    if not email or not usuario or not nome or not tipo or not senha1:
        messages.add_message(request, messages.WARNING, 'Todos os campos são obrigatórios')
        return render(request, 'home/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.add_message(request, messages.WARNING, 'email inválido')
        return render(request, 'aluno/cadastrar.html')

    if len(senha1) < 6:
        messages.add_message(request, messages.WARNING, 'Senha deve ter no mínimo 6 caracter')
        return render(request, 'home/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.add_message(request, messages.WARNING, 'Usuário já existe')
        return render(request, 'home/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.add_message(request, messages.WARNING, 'e-mail já existe')
        return render(request, 'home/cadastro.html')

    user = User.objects.create_user(
        username=usuario,
        email=email,
        first_name=nome,
        last_name=tipo,
        password=senha1
    )
    messages.add_message(request, messages.SUCCESS, 'Cadastrado com sucesso')
    user.save()
    return redirect('login')


def login(request):
    if request.method != 'POST':
        return render(request, 'home/login.html')

    usuario = request.POST.get('usuario')
    senha1 = request.POST.get('senha1')
    user = auth.authenticate(request, username=usuario, password=senha1)
    if not user:
        messages.add_message(request, messages.ERROR, 'Usuario ou senha invalidos')
        return render(request, 'home/login.html')
    else:
        auth.login(request, user)
        return redirect('principal')
