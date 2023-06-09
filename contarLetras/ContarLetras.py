import unittest

def contar_palabras(string):
    # Crear un diccionario vacío para contar las palabras
    result = {}

    # Convertir el string en una lista de palabras
    palabras = string.split()

    # Iterar sobre la lista de palabras
    for palabra in palabras:
        # Si la palabra ya está en el diccionario, incrementar el contador
        if palabra in result:
            result[palabra] += 1
        # Si la palabra no está en el diccionario, agregarla con un contador de 1
        else:
            result[palabra] = 1

    # Devolver el diccionario resultante
    return result

