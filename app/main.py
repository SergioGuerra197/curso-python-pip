import reader
import functions
# Funciones:
# 1 ) Mostrar jugadores jovenes (entre 18 y 22 años de edad) que hayan marcado al menos un gol den la liga.
# 2 ) Jugadores del barcelona con su numero de asistencias en la liga en un grafico de barras.
# 3 ) Grafico de pie en el que se muestren los jugadores de un equipo con su porcentaje sobre el 100% de los goles del equipo


def run():
    datos = reader.readCsv('./jugadores.csv')
    functions.menu(datos)


if __name__ == '__main__':
    run()
