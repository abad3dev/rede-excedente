
from django import forms
from instituicao.models import Instituicao


class InstituicaoForm(forms.ModelForm): 
    class Meta:
        model = Instituicao
        exclude = ['usuario']