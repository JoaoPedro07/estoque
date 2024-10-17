from rest_framework import serializers
from .models import Produto, ProdutoGroup


class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    produtos = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="produto-detail")
    grupo = serializers.PrimaryKeyRelatedField(queryset=ProdutoGroup.objects.all())
    class Meta:
        model = Produto
        fields = ('produto', 'grupo', 'detalhe', 'codigo', 'estoque', 'custo', 'marca', 'produtos')

class ProdutoGroupSerializer(serializers.HyperlinkedModelSerializer):
    categorias = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="produtogroup-detail")
    
    class Meta:
        model = ProdutoGroup
        fields = ('name', 'categorias')