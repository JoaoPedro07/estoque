from django.db import models

# Create your models here.

class ProdutoGroup(models.Model):
    name = models.CharField(max_length=250)
    
    class Meta:
        ordering = ("name", )
        
    def __str__(self):
        return self.name
    
class Produto(models.Model):
    produto = models.CharField(max_length=240)
    grupo = models.ForeignKey(
        ProdutoGroup, 
        max_length=240,
        related_name="grupos",
        on_delete=models.CASCADE
        )
    detalhe = models.TextField(max_length=700)
    codigo = models.IntegerField(primary_key=True)
    estoque = models.IntegerField()
    custo = models.FloatField()
    marca = models.CharField(max_length=50)
    
    def __str__(self):
        return self.codigo