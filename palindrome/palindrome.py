import unittest

def palindromo(word):
    # Eliminar espacios y convertir a minúsculas
    word = word.replace(" ", "").lower()
    
    # Verificar si la cadena es igual a su inversa
    if word == word[::-1]:
        return True
    else:
        return False
 
    
class TestPalindrome(unittest.TestCase):
    def test_palindrome_simple(self):
        result = palindromo('neuquen')
        self.assertEqual(result, True)

    def test_palindrome_complex(self):
        result = palindromo('anita laba la tina')   
        self.assertEqual(result, True)  
        
    def test_palindorme_complex2(self):
        result = palindromo('ana') 
        self.assertEqual(result, True)   

    def test_palindorme_complex3(self):
        result = palindromo('amor a roma') 
        self.assertEqual(result, True)
        
    def test_palindorme_complex4(self):
        result = palindromo('radar') 
        self.assertEqual(result, True)    

if __name__ == '__main__':
    unittest.main()