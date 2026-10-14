
from django import forms
from instituicao.models import Instituicao


class InstituicaoForm(forms.ModelForm): 
    class Meta:
        model = Instituicao
        fields = ['cnpj', 'nome', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'site', 'contato', 'telefone']