import requests


def get_categorias():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)  # Codigo de estado de la petición
    print(r.text)  # Visualizar la salida del request
    print(type(r.text))  # Es un string, hay que trasnformarlo
    categorias = r.json()
    for categoria in categorias:
        print(categoria['name'])
