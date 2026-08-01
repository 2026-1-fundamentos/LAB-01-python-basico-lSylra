"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    resultados = {}
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            letra = columnas[0]
            valor = int(columnas[1])
            if letra not in resultados:
                resultados[letra] = [valor, valor]
            else:
                if valor > resultados[letra][0]:
                    resultados[letra][0] = valor
                if valor < resultados[letra][1]:
                    resultados[letra][1] = valor

    lista_resultados = [(letra, max_min[0], max_min[1]) for letra, max_min in sorted(resultados.items())]
    return lista_resultados