from django.db import models

class Vinculados(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=12)
    cpf = models.CharField(max_length=11)
    entrada = models.DateTimeField(null=True, default = None)
    saida = models.DateTimeField(null=True, default = None)

class Visitante(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    entrada = models.DateTimeField(null=True, default = None)
    saida = models.DateTimeField(null=True, default = None)

class Porteiro(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    matricula = models.CharField(max_length=12)