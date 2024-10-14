from rest_framework import serializers
from .models import Produto


class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    produtos = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="produto-detail")
    
    class Meta:
        model = Produto
        fields = ('produto', 'grupo', 'detalhe', 'codigo', 'estoque', 'custo', 'marca', 'produtos')