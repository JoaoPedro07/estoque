import requests
url = "http://localhost:8000/produtos/"
codigo = '13131313'
data = {"estoque":90}
class PatchProduto:
    def patch_produto(url, codigo, data):
        response = requests.patch(url=(url+codigo), data=data)
        return response.status_code

def test_get_produto():
    assert PatchProduto.patch_produto(url, codigo, data) == 200
