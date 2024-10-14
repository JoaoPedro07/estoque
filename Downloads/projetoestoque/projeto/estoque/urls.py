from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("produtos/", 
         views.ProdutoList.as_view(), 
         name=views.ProdutoList.name),
    path("produtos/<int:pk>", 
         views.ProdutoDetail.as_view(), 
         name=views.ProdutoDetail.name),
    
]