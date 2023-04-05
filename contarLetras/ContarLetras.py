import unittest



import unittest



def count_letters(word):
    result = {}
    for letter in word:
        result[letter] = -1
    return result



class TestCountLetters (unittest.TestCase):
    
    def test_simple(self):
        result = count_letters('a')
        self.assertEqual(result, {'a': 1})
        
    def test_complex(self):
        result = count_letters('hola')
        self.assertEqual(result, {'hola': 1})    


