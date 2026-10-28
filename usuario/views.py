from urllib import request

from django.contrib import messages

from django.shortcuts import redirect, render

from usuario.forms import UsuarioForm
from django.contrib.auth.decorators import login_required

from usuario.models import Cidade
from material.models import Material, TipoMaterial

@login_required
def iniciar(request):
    materiais = Material.objects.all()
    tipomateriais = TipoMaterial.objects.all()
    return render(request, 'iniciar.html', {'materiais': materiais})

@login_required
def cadastrar_usuario(request):
    # 1. Proteção: Se o usuário já tem usuário, manda pro sistema e barra a tela de cadastro
    if hasattr(request.user, 'usuario'):
        return redirect('iniciar') 
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
    
            novo_usuario = form.save(commit=False)
    
            novo_usuario.usuario = request.user 
    
            novo_usuario.save()
            
            messages.success(request, 'Usuário cadastrado com sucesso!')
    
            return redirect('iniciar') 
        else:
            print("Erros do formulário:", form.errors)
            messages.error(request, 'Erro ao cadastrar. Verifique os dados e tente novamente.')
    else:
        form = UsuarioForm()

    cidades = Cidade.objects.all().order_by('nome')
       
    return render(request, 'cadastrar_usuario.html', {'form': form, 'cidades': cidades})