from pyexpat.errors import messages

from django.shortcuts import redirect, render

from instituicao.forms import InstituicaoForm
from django.contrib.auth.decorators import login_required

@login_required
def cadastrar_instituicao(request):
    # 1. Proteção: Se o usuário já tem instituição, manda pro sistema e barra a tela de cadastro
    if hasattr(request.user, 'instituicao'):
        return redirect('home') # Substitua 'home' pelo nome da URL da tela inicial do seu sistema

    if request.method == 'POST':
        form = InstituicaoForm(request.POST)
        if form.is_valid():
    
            nova_instituicao = form.save(commit=False)
    
            nova_instituicao.usuario = request.user 
    
            nova_instituicao.save()
            
            messages.success(request, 'Instituição cadastrada com sucesso!')
    
            return redirect('home') 
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados e tente novamente.')
    else:
        form = InstituicaoForm()
    
    
    return render(request, 'cad_instituicao.html', {'form': form})