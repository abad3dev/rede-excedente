from django import forms
from disponibilidade.models import Disponibilidade


class DisponibilidadeForm(forms.ModelForm): 
    class Meta:
        model = Disponibilidade
        fields = ['id_usuario', 'id_material', 'quantidade', 'valor_estimado']


class DisponibilidadeForm(forms.ModelForm): 
    class Meta:
        model = Disponibilidade
        fields = ['id_usuario', 'id_material', 'quantidade', 'valor_estimado']