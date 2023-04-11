import unittest
from palindromos import palindromos

class TestPalindrome(unittest.TestCase):
    def test_palindrome_simple(self):
        result = palindromos('neuquen')
        self.assertEqual(result, True)

    def test_palindrome_complex(self):
        result = palindromos('anita laba la tina')   
        self.assertEqual(result, True)  
        
    def test_palindorme_complex2(self):
        result = palindromos('ana') 
        self.assertEqual(result, True)   

    def test_palindorme_complex3(self):
        result = palindromos('amor a roma') 
        self.assertEqual(result, True)
        
    def test_palindorme_complex4(self):
        result = palindromos('radar') 
        self.assertEqual(result, True)    

if __name__ == '__main__':
    unittest.main()
