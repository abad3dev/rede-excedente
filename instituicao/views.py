from urllib import request

from django.contrib import messages

from django.shortcuts import redirect, render

from instituicao.forms import InstituicaoForm
from django.contrib.auth.decorators import login_required

from instituicao.models import Cidade
from material.models import Material, TipoMaterial

@login_required
def iniciar(request):
    materiais = Material.objects.all()
    tipomateriais = TipoMaterial.objects.all()
    return render(request, 'iniciar.html', {'materiais': materiais})

@login_required
def cadastrar_instituicao(request):
    # 1. Proteção: Se o usuário já tem instituição, manda pro sistema e barra a tela de cadastro
    if hasattr(request.user, 'instituicao'):
        return redirect('iniciar') 
    
    if request.method == 'POST':
        form = InstituicaoForm(request.POST)
        if form.is_valid():
    
            nova_instituicao = form.save(commit=False)
    
            nova_instituicao.usuario = request.user 
    
            nova_instituicao.save()
            
            messages.success(request, 'Instituição cadastrada com sucesso!')
    
            return redirect('iniciar') 
        else:
            print("Erros do formulário:", form.errors)
            messages.error(request, 'Erro ao cadastrar. Verifique os dados e tente novamente.')
    else:
        form = InstituicaoForm()

    cidades = Cidade.objects.all().order_by('nome')
       
    return render(request, 'cadastrar_instituicao.html', {'form': form, 'cidades': cidades})