from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from disponibilidade.forms import DisponibilidadeForm
from disponibilidade.models import Disponibilidade
from material.models import Material
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def disponibilizar(request, id_material):

    if request.method == 'POST':
        form = DisponibilidadeForm(request.POST)
        if form.is_valid():
    
            nova_disponibilidade = form.save(commit=False)
    
            nova_disponibilidade.save()
            
            messages.success(request, 'Material cadastrado com sucesso!')
    
            return redirect('iniciar') 
        else:
            print("Erros do formulário:", form.errors)
            messages.error(request, 'Erro ao cadastrar. Verifique os dados e tente novamente.')
    else:   

        id_instituicao = request.session.get('id_inst')
        quantidades = range(1, 1001)
        material_selecionado = get_object_or_404(Material, id_material=id_material)
        materiais = Material.objects.all()
        return render(request, 'disponibilizar_material.html', {'id_material': id_material, 'quantidades': quantidades, 'materiais': materiais, 'id_instituicao': id_instituicao})


@login_required
def consultar_minhasdoacoes(request):

    id_instituicao = request.session.get('id_inst')

    disponibilidades = Disponibilidade.objects.filter(id_instituicao=id_instituicao).select_related('id_material')

    for disponibilidade in disponibilidades:
        disponibilidade.valor_total = disponibilidade.quantidade * disponibilidade.valor_estimado

    return render(request, 'consultar_minhasdoacoes.html', {'disponibilidades': disponibilidades})