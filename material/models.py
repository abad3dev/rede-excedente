from django.db import models


from usuario.models import Usuario

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

class UsuarioTipoMaterial(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    id_tipo_material = models.ForeignKey(TipoMaterial, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id_usuario.nome} - {self.id_tipo_material.tipo}"




