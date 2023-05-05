import matplotlib.pyplot as plt


def generarGraficoBarras(nombres, valores):
    fig, ax = plt.subplots()
    ax.bar(nombres, valores)
    plt.xticks(rotation=90)
    plt.savefig('./imgs/bar.png')
    plt.close()


def generarGraficoPie(equipo, nombres, valores):
    fig, ax = plt.subplots()
    # Le indicamos directamente como son los labels
    ax.pie(valores, labels=nombres, autopct="%0.1f %%")
    # Se le indica que ponga la grafica en el centro y que sea en forma de circulo
    ax.axis('equal')
    plt.savefig(f'./imgs/{equipo}.png')
    plt.close()
