from django.db import models

from instituicao.models import Instituicao
from material.models import Material

# Create your models here.

# Create your models here.
class Disponibilidade(models.Model):
    id_disponibilidade = models.AutoField(primary_key=True)
    id_instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    id_material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_publicacao = models.DateField(auto_now_add=True)
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id_instituicao.nome} - {self.id_material.descricao} - {self.quantidade}"