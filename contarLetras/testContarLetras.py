import unittest
from ContarLetras import contar_palabras

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