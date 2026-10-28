from django.db import models


from material.models import Material
from usuario.models import Usuario


# Create your models here.
class Disponibilidade(models.Model):
    id_disponibilidade = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_publicacao = models.DateField(auto_now_add=True)
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    arquivo = models.FileField(upload_to='disponibilidade/arquivos/', null=True, blank=True)

    def __str__(self):
        return f"{self.id_usuario.nome} - {self.id_material.descricao} - {self.quantidade}"