import requests
url = "http://localhost:8000/produtos/"
codigo = '13131313'

class GetProduto:
    def get_produto(url, codigo):
        response = requests.get(url+codigo)
        return response.status_code

def test_get_produto():
    assert GetProduto.get_produto(url, codigo) == 200