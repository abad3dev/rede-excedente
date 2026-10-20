from django.core.checks import messages
from django.shortcuts import redirect, render
from material.forms import MaterialForm
from material.models import TipoMaterial
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cadastrar_material(request):

    
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
    
            novo_material = form.save(commit=False)
    
            novo_material.usuario = request.user 
    
            novo_material.save()
            
            messages.success(request, 'Material cadastrado com sucesso!')
    
            return redirect('iniciar') 
        else:
            print("Erros do formulário:", form.errors)
            messages.error(request, 'Erro ao cadastrar. Verifique os dados e tente novamente.')
    else:
        form = MaterialForm()

    tipomateriais = TipoMaterial.objects.all().order_by('tipo')
       
    return render(request, 'cadastrar_material.html', {'form': form, 'tipomateriais': tipomateriais})