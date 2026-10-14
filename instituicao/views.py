from pyexpat.errors import messages

from django.shortcuts import redirect, render

from instituicao.forms import InstituicaoForm

# Create your views here.
def cadastrar_instituicao(request):
    if request.method == 'POST':
        form = InstituicaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Instituição cadastrada com sucesso!')
            return redirect('cadastrar_instituicao')
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados e tente novamente.')

    else:
        form = InstituicaoForm()
    
    return render(request, 'cad_instituicao.html')