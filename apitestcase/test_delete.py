import requests
from test_getEspecific import GetProduto
url = "http://localhost:8000/produtos/"
codigo = '12121212'

class DeleteProduto:
    def delete_produto(url, codigo):
        response = requests.delete(url+codigo)
        return response.status_code

def teste_delete_produto():
    assert DeleteProduto.delete_produto(url, codigo) == 204
    assert GetProduto.get_produto(url, codigo) == 404