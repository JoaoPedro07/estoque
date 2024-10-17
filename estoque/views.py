from django.shortcuts import render
from rest_framework import generics, viewsets
from estoque.serializers import ProdutoSerializer, ProdutoGroupSerializer
from estoque.models import Produto, ProdutoGroup

# Create your views here.

class ProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    name = 'produto-list'

class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    name = 'produto-detail'


class ProdutoGroupList(generics.ListCreateAPIView):
    queryset = ProdutoGroup.objects.all()
    serializer_class = ProdutoGroupSerializer
    name = "produtogroup-list"

class ProdutoGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProdutoGroup.objects.all()
    serializer_class = ProdutoGroupSerializer
    name = "produtogroup-detail"