import csv


def readCsv(ruta):  # recibe la ruta del csv
    # abre el csv, determinando que es solo operacion de lectura
    with open(ruta, 'r', encoding='UTF-8') as jugadoresCsv:
        # declara el lector del csv
        reader = csv.reader(jugadoresCsv, delimiter=',')
        # Los header se encuentran en la primera fila del csv, por eso se hace y se guarda el next
        header = next(reader)
        datos = []  # array donde quedará las filas en forma de diccionario
        for row in reader:
            iterable = zip(header, row)
            jugadores_dict = {key: value for key, value in iterable}
            datos.append(jugadores_dict)
        return datos


if __name__ == '__main__':
    datos = readCsv('./jugadores.csv')
    print(datos)
