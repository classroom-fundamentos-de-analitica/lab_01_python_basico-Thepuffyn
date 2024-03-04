"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("data.csv", 'r') as file:
        timesheet = file.readlines()
    
    timesheet = [row.replace('\n', '') for row in timesheet]
    timesheet = [row.replace('\t', ',') for row in timesheet]
    timesheet = [row.split(',') for row in timesheet]
    
    suma = 0

    for i in range(len(timesheet)):
        suma += int(timesheet[i][1])    

    return suma



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open("data.csv", 'r') as file:
        timesheet = file.readlines()
    
    timesheet = [row.replace('\n', '') for row in timesheet]
    timesheet = [row.replace('\t', ',') for row in timesheet]
    timesheet = [row.split(',') for row in timesheet]
    
    resultado = []
    resultado.append([timesheet[0][0], 1])

    for i in range(1, len(timesheet)):
        encontrado = False
        for j in range(len(resultado)):
            if resultado[j][0] == timesheet[i][0]:
                resultado[j][1] += 1
                encontrado = True
                break
        
        if not encontrado:
            resultado.append([timesheet[i][0], 1])

    resultado = [tuple(x) for x in resultado]
    resultado.sort()
    return resultado


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open("data.csv", 'r') as file:
        timesheet = file.readlines()
    
    timesheet = [row.replace('\n', '') for row in timesheet]
    timesheet = [row.replace('\t', ',') for row in timesheet]
    timesheet = [row.split(',') for row in timesheet]
    
    resultado = []
    resultado.append([timesheet[0][0], int(timesheet[0][1])])

    for i in range(1, len(timesheet)):
        encontrado = False
        for j in range(len(resultado)):
            if resultado[j][0] == timesheet[i][0]:
                resultado[j][1] += int(timesheet[i][1])
                encontrado = True
                break
        
        if not encontrado:
            resultado.append([timesheet[i][0], int(timesheet[i][1])])

    resultado = [tuple(x) for x in resultado]
    resultado.sort()
    return resultado


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv", 'r') as file:
        timesheet = file.readlines()
    
    timesheet = [row.replace('\n', '') for row in timesheet]
    timesheet = [row.replace('\t', ',') for row in timesheet]
    timesheet = [row.split(',') for row in timesheet]
    
    resultado = []
    resultado.append([timesheet[0][2].split('-')[1], 1])
    
    for i in range(1, len(timesheet)):
        encontrado = False
        fecha = timesheet[i][2].split('-')
        for j in range(len(resultado)):
            if resultado[j][0] == fecha[1]:
                resultado[j][1] += 1
                encontrado = True
                break
        if not encontrado:
            resultado.append([fecha[1], 1])

    resultado = [tuple(x) for x in resultado]
    resultado.sort()
    return resultado


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv", 'r') as file:
        timesheet = file.readlines()
    
    timesheet = [row.replace('\n', '') for row in timesheet]
    timesheet = [row.replace('\t', ',') for row in timesheet]
    timesheet = [row.split(',') for row in timesheet]
    
    resultado = []
    resultado.append([timesheet[0][0], int(timesheet[0][1]), int(timesheet[0][1])])

    for i in range(1, len(timesheet)):
        encontrado = False
        for j in range(len(resultado)):
            if timesheet[i][0] == resultado[j][0]:
                if int(timesheet[i][1]) > resultado[j][1]:
                    resultado[j][1] = int(timesheet[i][1])
                elif int(timesheet[i][1]) < resultado[j][2]:
                    resultado[j][2] = int(timesheet[i][1])
                encontrado = True
                break
        
        if not encontrado:
            print(timesheet[i][0])
            resultado.append([timesheet[i][0], int(timesheet[i][1]), int(timesheet[i][1])])

    resultado = [tuple(x) for x in resultado]
    resultado.sort()
    return resultado


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv", 'r') as file:
        timesheet = file.readlines()
    
    timesheet = [row.replace('\n', '') for row in timesheet]
    timesheet = [row.replace(',', ':') for row in timesheet]
    timesheet = [row.replace('\t', ',') for row in timesheet]
    timesheet = [row.split(',') for row in timesheet]
    
    resultado = []
    resultado.append([timesheet[0][4].split(':')[0], int(timesheet[0][4].split(':')[1]), int(timesheet[0][4].split(':')[1])])

    for i in range(len(timesheet)):
        registro = timesheet[i][4].split(':')
        inicio = 0
        if i == 0:
            inicio = 2
        for k in range(inicio, len(registro), 2):
            encontrado = False
            for j in range(len(resultado)):
                if resultado[j][0] == registro[k]:
                    if int(registro[k + 1]) > resultado[j][2]:
                        resultado[j][2] = int(registro[k + 1])
                    elif int(registro[k + 1]) < resultado[j][1]:
                        resultado[j][1] = int(registro[k + 1])
                    encontrado = True
                    break
        
            if not encontrado:
                resultado.append([registro[k], int(registro[k + 1]), int(registro[k + 1])])

    resultado = [tuple(x) for x in resultado]
    resultado.sort()
    return resultado


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv", 'r') as file:
        timesheet = file.readlines()
    
    timesheet = [row.replace('\n', '') for row in timesheet]
    timesheet = [row.replace('\t', ',') for row in timesheet]
    timesheet = [row.split(',') for row in timesheet]
    
    resultado = []
    resultado.append([int(timesheet[0][1]), [timesheet[0][0]]])

    for i in range(1, len(timesheet)):
        encontrado = False
        for j in range(len(resultado)):
            if resultado[j][0] == int(timesheet[i][1]):
                resultado[j][1].append(timesheet[i][0])
                encontrado = True
                break
        
        if not encontrado:
            resultado.append([int(timesheet[i][1]), [timesheet[i][0]]])

    resultado = [tuple(x) for x in resultado]
    resultado.sort()
    return resultado


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv", 'r') as file:
        timesheet = file.readlines()
    
    timesheet = [row.replace('\n', '') for row in timesheet]
    timesheet = [row.replace('\t', ',') for row in timesheet]
    timesheet = [row.split(',') for row in timesheet]
    
    resultado = []
    resultado.append([int(timesheet[0][1]), [timesheet[0][0]]])

    for i in range(1, len(timesheet)):
        encontrado = False
        for j in range(len(resultado)):
            if resultado[j][0] == int(timesheet[i][1]):
                if timesheet[i][0] not in resultado[j][1]:
                    resultado[j][1].append(timesheet[i][0])
                encontrado = True
                break
        
        if not encontrado:
            resultado.append([int(timesheet[i][1]), [timesheet[i][0]]])

    resultado = [[x[0], sorted(x[1])] for x in resultado]
    resultado = [tuple(x) for x in resultado]
    resultado.sort()
    return resultado


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open("data.csv", 'r') as file:
        timesheet = file.readlines()
    
    timesheet = [row.replace('\n', '') for row in timesheet]
    timesheet = [row.replace(',', ':') for row in timesheet]
    timesheet = [row.replace('\t', ',') for row in timesheet]
    timesheet = [row.split(',') for row in timesheet]
    
    resultado = {}
    resultado[timesheet[0][4].split(':')[0]] = 1

    for i in range(len(timesheet)):
        registro = timesheet[i][4].split(':')
        inicio = 0
        if i == 0:
            inicio = 2
        for k in range(inicio, len(registro), 2):
            encontrado = False
            for j in resultado:
                if j == registro[k]:
                    resultado[j] += 1
                    encontrado = True
                    break
        
            if not encontrado:
                resultado[registro[k]] = 1
    resultado1 = sorted(resultado)
    resultado2 = {}
    
    for i in resultado1:
        resultado2[i] = resultado[i]
    return resultado2


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("data.csv", 'r') as file:
        timesheet = file.readlines()
    
    timesheet = [row.replace('\n', '') for row in timesheet]
    timesheet = [row.replace(',', '-') for row in timesheet]
    timesheet = [row.replace('\t', ',') for row in timesheet]
    timesheet = [row.split(',') for row in timesheet]
    
    resultado = []

    for i in range(len(timesheet)):
        resultado.append((timesheet[i][0], len(timesheet[i][3].split('-')), len(timesheet[i][4].split('-'))))

    return resultado


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open("data.csv", 'r') as file:
        timesheet = file.readlines()
    
    timesheet = [row.replace('\n', '') for row in timesheet]
    timesheet = [row.replace(',', '-') for row in timesheet]
    timesheet = [row.replace('\t', ',') for row in timesheet]
    timesheet = [row.split(',') for row in timesheet]
    
    resultado = []
    resultado.append([timesheet[0][3].split('-')[0], int(timesheet[0][1])])
    
    for i in range(len(timesheet)):
        columna4 = timesheet[i][3].split('-')
        inicio = 0
        if i == 0:
            inicio = 1
                    
        for k in range(inicio, len(columna4)):
            encontrado = False
            
            for j in range(len(resultado)):
                if resultado[j][0] == columna4[k]:
                    resultado[j][1] += int(timesheet[i][1])
                    encontrado = True
                    break
        
            if not encontrado:
                resultado.append([columna4[k], int(timesheet[i][1])])
    
    resultado.sort()
    resultado1 = {}
    
    for i in resultado:
        resultado1[i[0]] = i[1]
    
    return resultado1


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("data.csv", 'r') as file:
        timesheet = file.readlines()
    
    timesheet = [row.replace('\n', '') for row in timesheet]
    timesheet = [row.replace(',', ':') for row in timesheet]
    timesheet = [row.replace('\t', ',') for row in timesheet]
    timesheet = [row.split(',') for row in timesheet]
    
    resultado = []
    resultado.append([timesheet[0][0], int(timesheet[0][4].split(':')[1])])
    
    for i in range(len(timesheet)):
        columna5 = timesheet[i][4].split(':')
        inicio = 1
        
        if i == 0:
            inicio = 3
                    
        for k in range(inicio, len(columna5), 2):
            encontrado = False

            for j in range(len(resultado)):
                if resultado[j][0] == timesheet[i][0]:
                    resultado[j][1] += int(columna5[k])
                    encontrado = True
                    break
        
            if not encontrado:
                resultado.append([timesheet[i][0], int(columna5[k])])
    
    resultado.sort()
    resultado1 = {}
    
    for i in resultado:
        resultado1[i[0]] = i[1]
    
    return resultado1
