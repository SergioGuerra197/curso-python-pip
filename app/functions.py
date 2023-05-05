import charts
import functions


def menu(datos):
    print('Bienvenido!!')
    while True:
        print("1. Mostrar jugadores jovenes (entre 18 y 22 años de edad) que hayan marcado al menos un gol den la liga.")
        print("2. Jugadores del barcelona con su numero de asistencias en la liga en un grafico de barras.")
        print("3. Grafico de pie en el que se muestren los jugadores de un equipo con su porcentaje sobre el 100% de los goles del equipo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            functions.jugadoresJovenes(datos)
        elif opcion == "2":
            functions.asist(datos)
        elif opcion == "3":
            functions.equipos(datos)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción válida.")


def jugadoresJovenes(datos):
    datos = list(
        filter(lambda item: int(item['Age']) in range(17, 23) and item['Goals'] != '' and int(item['Goals']) >= 2, datos))
    nombres = list(map(lambda item: item['Player Name'], datos))
    goles = list(map(lambda item: item['Goals'], datos))
    nombres = list(zip(nombres, goles))
    for i in range(len(nombres)):
        print('*'*10)
        # Se muestra la tupla, el primer corchete es la posicion y el segundo es la posicion interna de la tupla
        print('Nombre:', nombres[i][0], '|  Goles:', nombres[i][1])


def asist(datos):
    nombresOrdenados = []
    asistenciasOrdenadas = []
    datos = list(filter(
        lambda item: item['Team-name'] == 'Barcelona' and item['Assist'] != '', datos))
    nombres = list(map(lambda item: item['Player Name'], datos))
    asistencias = list(map(lambda item: item['Assist'], datos))
    orden = list(zip(nombres, asistencias))
    listaOrdenada = sorted(orden, key=lambda x: x[1])
    for i in range(len(listaOrdenada)):
        nombresOrdenados.append(listaOrdenada[i][0])
        asistenciasOrdenadas.append(listaOrdenada[i][1])
    charts.generarGraficoBarras(nombresOrdenados, asistenciasOrdenadas)


def equipos(datos):
    nombresOrdenados = []
    golesOrdenados = []
    equipos = set(map(lambda item: item['Team-name'], datos))
    print('Los equipos de la liga son =>', equipos)
    nombre = input('Ingrese el nombre del equipo que desea=> ').lower().title()
    datos = list(
        filter(lambda item: item['Team-name'] == nombre and item['Goals'] != '', datos))
    print(datos)
    nombres = list(map(lambda item: item['Player Name'], datos))
    goles = list(map(lambda item: item['Goals'], datos))
    orden = list(zip(nombres, goles))
    for i in range(len(orden)):
        nombresOrdenados.append(orden[i][0])
        golesOrdenados.append(orden[i][1])
    charts.generarGraficoPie(nombre,nombresOrdenados, golesOrdenados)


if __name__ == '__main__':
    jugadoresJovenes('./jugadores.csv')
