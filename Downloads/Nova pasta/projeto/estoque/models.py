from django.db import models

# Create your models here.

class Produto(models.Model):
    produto = models.CharField(max_length=240)
    grupo = models.CharField(max_length=240)
    detalhe = models.TextField(max_length=700)
    codigo = models.IntegerField(primary_key=True)
    estoque = models.IntegerField()
    custo = models.FloatField()
    marca = models.CharField(max_length=50)
    
    def __str__(self):
        return self.codigo