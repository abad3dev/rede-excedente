from django.db import models


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


