import requests
url = "http://localhost:8000/produtos/"

class GetProdutos:
    def get_produtos(url):
        response = requests.get(url)
        return response.status_code

def test_get_produtos_answer():
    assert GetProdutos.get_produtos(url) == 200