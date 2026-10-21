from django import forms
from disponibilidade.models import Disponibilidade


class DisponibilidadeForm(forms.ModelForm): 
    class Meta:
        model = Disponibilidade
        fields = ['id_instituicao', 'id_material', 'quantidade', 'valor_estimado']