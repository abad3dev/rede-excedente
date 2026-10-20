

from material.models import Material
from django import forms


class MaterialForm(forms.ModelForm): 
    class Meta:
        model = Material
        fields = ['descricao', 'id_tipo_material']


