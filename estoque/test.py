from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Produto

class ProdutoTests(APITestCase):
    def test_create_produto(self):
        """
        Teste de criação de produto - Método POST
        
        """
        url = reverse('produto-list')
        data = {
            "produto": "Pastilha Garoto",
            "grupo": "doces",
            "detalhe": "Pastilha de hortela garoto 100g",
            "codigo": 12121212,
            "estoque": 20,
            "custo": 3.5,
            "marca": "Garoto"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.get().produto, 'Pastilha Garoto')
        
    def test_patch_produto(self):
        """
        Teste de criação de produto - Método POST
        
        """
        #Criação de um produtos para ter como exemplo de busca
        produto = Produto.objects.create(
            produto="Pastilha Garoto",
            grupo="doces",
            detalhe="Pastilha de hortela garoto 100g",
            codigo=12121212,
            estoque=20,
            custo=3.5,
            marca="Garoto"
        )
        url = reverse('produto-detail', kwargs={'pk':produto.pk})
        data = {
            "estoque": 20,
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Produto.objects.get().produto, 'Pastilha Garoto')

    def test_get_produtos(self):
        """
        Teste de obtenção de todos os produtos - Método GET
        
        """
        
        #Criação de um produtos para ter como exemplo de busca
        Produto.objects.create(
            produto="Pastilha Garoto",
            grupo="doces",
            detalhe="Pastilha de hortela garoto 100g",
            codigo=12121212,
            estoque=20,
            custo=3.5,
            marca="Garoto"
        )
        Produto.objects.create(
            produto="Energético Monster",
            grupo="Bebidas",
            detalhe="Energético Monster 700ml",
            codigo=13131313,
            estoque=20,
            custo=9.99,
            marca="Monster"
        )
        
        url = reverse('produto-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_produto_especifico(self):
        """
        Teste de obtenção de produto específico por identação - Método GET
        
        """
                
        #Criação de um produto para ter como exemplo de busca
        produto = Produto.objects.create(
            produto="Pastilha Garoto",
            grupo="doces",
            detalhe="Pastilha de hortela garoto 100g",
            codigo=12121212,
            estoque=20,
            custo=3.5,
            marca="Garoto"
        )

        url = reverse('produto-detail', kwargs={'pk':produto.pk})
        print("url:",url)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_produto_especifico(self):
        """
        Teste de obtenção de produto específico por identação - Método GET
        
        """
                
        #Criação de um produto para ter como exemplo de busca
        produto = Produto.objects.create(
            produto="Pastilha Garoto",
            grupo="doces",
            detalhe="Pastilha de hortela garoto 100g",
            codigo=12121212,
            estoque=20,
            custo=3.5,
            marca="Garoto"
        )

        url = reverse('produto-detail', kwargs={'pk':produto.pk})
        print("url:",url)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


