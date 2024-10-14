from django.shortcuts import render
from rest_framework import generics
from estoque.serializers import ProdutoSerializer
from estoque.models import Produto

# Create your views here.

class ProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    name = 'produto-list'

class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    name = 'produto-detail'