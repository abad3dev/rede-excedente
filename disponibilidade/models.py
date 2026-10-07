from django.db import models

# Create your models here.

class Instituicao(models.Model):
    id_inst = models.AutoField(primary_key=True)
    cnpj = models.CharField(max_length=18, unique=True)
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    site = models.URLField(max_length=200, blank=True, null=True)
    contato = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    id_cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2, unique=True)
    
    def __str__(self):
        return self.nome

class Cidade(models.Model):
    id_cidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

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

class Disponibilidade(models.Model):
    id_disponibilidade = models.AutoField(primary_key=True)
    id_instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    id_material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_publicacao = models.DateField(auto_now_add=True)
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.id_instituicao.nome} - {self.id_material.descricao} - {self.quantidade}"