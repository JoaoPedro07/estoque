from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Produto, ProdutoGroup

class ProdutoTests(APITestCase):
    def setUp(self):
        #Criando objetos de grupo de produtos e produtos no banco de dados para utilização nos testes
        self.doce = ProdutoGroup.objects.create(name="Doces") 
        self.bebidas = ProdutoGroup.objects.create(name="Bebidas")
        self.produto = Produto.objects.create(
            produto="Pastilha Garoto",
            grupo=self.doce,
            detalhe="Pastilha de hortela garoto 100g",
            codigo=12121212,
            estoque=20,
            custo=3.5,
            marca="Garoto"
        )
        
    def test_create_produto(self):
        """
        [001] Teste de criação de produto - Método POST
        
        """
        #obter url do endpoint
        url = reverse('produto-list')
        data = {
            "produto": "Bombom Garoto",
            "grupo": self.doce.id,
            "detalhe": "Bombom Garoto 40g",
            "codigo": 14141414,
            "estoque": 20,
            "custo": 3.5,
            "marca": "Garoto"
        }
        
        #solicitar alteração ao endpoint
        response = self.client.post(url, data, format='json')
        
        #testar se o status code confere com o que foi solicitado
        # e se a alteração solicitada foi atendida
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.get(codigo=14141414).produto, "Bombom Garoto")
        
    def test_patch_produto(self):
        """
        [002] Teste de alteração de produto - Método PATCH
        
        """
        #obter url do endpoint
        url = reverse('produto-detail', kwargs={'pk':self.produto.pk})
        data = {
            "estoque": 20,
        }
        
        #solicitar alteração ao endpoint
        response = self.client.patch(url, data, format='json')
        
        #testar se o status code confere com o que foi solicitado
        # e se a alteração solicitada foi atendida
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Produto.objects.get(codigo=self.produto.codigo).estoque, 20)

    def test_get_produtos(self):
        """
        [003] Teste de obtenção de todos os produtos - Método GET
        
        """
        #obter url do endpoint        
        url = reverse('produto-list')
        
        #solicitar alteração ao endpoint
        response = self.client.get(url, format='json')

        #testar se o status code confere com o que foi solicitado
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_produto_especifico(self):
        """
        [004] Teste de obtenção de produto específico por identação - Método GET
        
        """
        #obter url do endpoint        
        url = reverse('produto-detail', kwargs={'pk':self.produto.pk})

        #solicitar ao endpoint
        response = self.client.get(url, format='json')
        
        #testar se o status code confere com o que foi solicitado
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_produto(self):
        """
        [005] Teste de exclusão de um produto por identação - Método DELETE
        
        """
        #obter url do endpoint        
        url = reverse('produto-detail', kwargs={'pk':self.produto.pk})
        
        #solicitar alteração ao endpoint
        response = self.client.delete(url, format='json')
        
        #testar se o status code confere com o que foi solicitado
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_grupo(self):
        """
        [006] Teste de criação de grupo - Método POST
        
        """
        #obter url do endpoint
        url = reverse('produtogroup-list')
        data = {
            "name":"Biscoitos"
        }
        
        #solicitar alteração ao endpoint
        response = self.client.post(url, data, format='json')
        
        #testar se o status code confere com o que foi solicitado
        # e se o produto foi criado 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProdutoGroup.objects.get(name="Biscoitos").name, "Biscoitos")
    
    def test_delete_grupo(self):
        """
        [007] Teste de exclusão de um grupo por identação - Método DELETE
        
        """
        #obter url do endpoint
        url = reverse('produtogroup-detail', kwargs={'pk':self.bebidas.id})

        #solicitar alteração
        response = self.client.delete(url, format='json')
        
        #testar se o status code confere com o que foi solicitado
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)