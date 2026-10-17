
import re
import requests
from django import forms
from django.core.exceptions import ValidationError
from instituicao.models import Instituicao


class InstituicaoForm(forms.ModelForm): 
    class Meta:
        model = Instituicao
        exclude = ['usuario']

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        
        if not cnpj:
            return cnpj

        # 1. Remove pontos, barras e traços (a API prefere receber apenas números)
        cnpj_numeros = re.sub(r'[^0-9]', '', str(cnpj))

        # 2. Consulta a BrasilAPI
        try:
            url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_numeros}"
            response = requests.get(url, timeout=5) 
            
            # Se a API retornar 404 (Not Found), significa que não existe na Receita
            if response.status_code == 404:
                raise ValidationError("Este CNPJ não consta na base da Receita Federal.")
            
            # Se retornar 400 (Bad Request), a API identificou que o CNPJ tem um tamanho/formato impossível
            elif response.status_code == 400:
                raise ValidationError("O formato do CNPJ é inválido.")
                
        except requests.Timeout:
            # Caso o servidor da BrasilAPI esteja lento ou fora do ar
            raise ValidationError("O serviço de validação está lento. Tente novamente em alguns segundos.")
            
        except requests.ConnectionError:
            # Caso haja problema de rede/internet no seu servidor
            raise ValidationError("Não foi possível conectar ao serviço de validação no momento.")

        # Se passou direto pelas validações (Status 200 OK), retorna o CNPJ limpo para salvar
        return cnpj_numeros