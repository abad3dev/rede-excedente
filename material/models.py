from django.db import models

from instituicao.models import Instituicao

class TipoMaterial(models.Model):
    id_tipo_material = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tipo

class Material(models.Model):
    id_material = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    id_tipo_material = models.ForeignKey(TipoMaterial, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descricao

class InstituicaoTipoMaterial(models.Model):
    id_instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    
    id_tipo_material = models.ForeignKey(TipoMaterial, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id_instituicao.nome} - {self.id_tipo_material.tipo}"




