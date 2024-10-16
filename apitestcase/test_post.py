import requests
url = "http://localhost:8000/produtos/"
data = {
    "produto": "Pastilha Garoto",
    "grupo": "doces",
    "detalhe": "Pastilha de hortela garoto 100g",
    "codigo": 12121212,
    "estoque": 21,
    "custo": 3.5,
    "marca": "Garoto"
}
class PostProduto:
    def post_produto(url, data):
        response = requests.post(url=url, json=data)
        return response.status_code

def test_get_produto():
    assert PostProduto.post_produto(url, data) == 201
