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

class TestContarPalabras(unittest.TestCase):
    def test_contar_palabras_simple(self):
        result = contar_palabras('Hola como estas hola')
        self.assertEqual(result, {'Hola': 1, 'como': 1, 'estas': 1, 'hola': 1})

    def test_contar_palabras_vacio(self):
        result = contar_palabras('')
        self.assertEqual(result, {})
        
    def test_contar_palabras_compleja(self):
        result = contar_palabras('aprobar la materia si o si')
        self.assertEqual(result, {'aprobar': 1, 'la': 1, 'materia': 1, 'si': 2, 'o': 1,})
        
        
    def test_contar_palabras_compleja2(self):
        result = contar_palabras('Hola, hoy tuve un dia muy complicado y triste Hola,')
        self.assertEqual(result, {'Hola,' : 2, 'hoy': 1, 'tuve': 1, 'un': 1, 'dia': 1, 'muy': 1, 'complicado': 1, 'y': 1, 'triste': 1, })    
        
        
    def test_contar_palabras_compleja3(self):
        result = contar_palabras('los profesores de la um, los mejores profesores')
        self.assertEqual(result, {'los' : 2, 'profesores': 2, 'de': 1, 'la': 1, 'um,': 1, 'mejores': 1, })     

    

if __name__ == '__main__':
    unittest.main()






















































































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