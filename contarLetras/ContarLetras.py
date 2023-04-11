import unittest

def contar_palabras(string):
    # Crear un diccionario vacío para contar las palabras
    contador = {}

    # Convertir el string en una lista de palabras
    palabras = string.split()

    # Iterar sobre la lista de palabras
    for palabra in palabras:
        # Si la palabra ya está en el diccionario, incrementar el contador
        if palabra in contador:
            contador[palabra] += 1
        # Si la palabra no está en el diccionario, agregarla con un contador de 1
        else:
            contador[palabra] = 1

    # Devolver el diccionario resultante
    return contador






















































































'''
import unittest

string = "Hola como estas hola"

def contar_palabras(string):
    # Crear un diccionario vacío para contar las palabras
    contador = {}

    # Convertir el string en una lista de palabras
    palabras = string.split()

    # Iterar sobre la lista de palabras
    for palabra in palabras:
        # Si la palabra ya está en el diccionario, incrementar el contador
        if palabra in contador:
            contador[palabra] += 1
        # Si la palabra no está en el diccionario, agregarla con un contador de 1
        else:
            contador[palabra] = 1

    # Devolver el diccionario resultante
    return contador



class TestCountLetters(unittest.TestCase):

    def test_simple(self):
        result = contar_palabras('a')
        self.assertEqual(result, {'a': 1})
        
    def test_complex(self):
        result = contar_palabras('hola')
        self.assertEqual(
            result,
            {
                'h': 1,
                'o': 1,
                'l': 1,
                'a': 1,
            }
        )

    def test_super_complex(self):
        result = contar_palabras('hola chau')
        self.assertEqual(
            result,
            {
                'h': 2,
                'o': 1,
                'l': 1,
                'a': 2,
                ' ': 1,
                'c': 1,
                'u': 1
            }
        )      
    
    
    def test_super_complex(self):
        result = contar_palabras('hola como estas chau hola')
        self.assertEqual(
            result,
            {
                'h': 3,
                'o': 4,
                'l': 2,
                'a': 4,
                ' ': 4,
                'c': 2,
                'u': 1,
                'm': 1,
                's': 2,
                'e': 1
            }
        )      
            
        
if __name__ == '__main__':
    unittest.main()        
'''