import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()  # Creamos instancia de la aplicacion


@app.get('/')  # Decotador
def get_lista():
    return [1, 2, 3]


@app.get('/contacto', response_class=HTMLResponse)  # Decotador
def get_lista():
    return """
        <h1>Hola soy una pagina</h1>
        <p>Soy un parrafo</p>
    """


def run():
    store.get_categorias()


if __name__ == '__main__':
    run()
