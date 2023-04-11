import unittest
from palindrome import palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome_simple(self):
        result = palindrome('neuquen')
        self.assertEqual(result, True)

    def test_palindrome_complex(self):
        result = palindrome('anita laba la tina')   
        self.assertEqual(result, True)  
        
    def test_palindorme_complex2(self):
        result = palindrome('ana') 
        self.assertEqual(result, True)   

    def test_palindorme_complex3(self):
        result = palindrome('amor a roma') 
        self.assertEqual(result, True)
        
    def test_palindorme_complex4(self):
        result = palindrome('radar') 
        self.assertEqual(result, True)    

if __name__ == '__main__':
    unittest.main()
