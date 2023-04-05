import unittest
from RomanosADecimal import roman_to_decimal

class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal('I')
        self.assertEqual(resultado, 1)

    def test_V(self):
        resultado = roman_to_decimal('V')
        self.assertEqual(resultado, 5)

    def test_X(self):
        resultado = roman_to_decimal('X')
        self.assertEqual(resultado, 10)
        
    def test_III(self):
        resultado = roman_to_decimal('III')
        self.assertEqual(resultado, 3)
            
    def test_II(self):
        resultado = roman_to_decimal('II')
        self.assertEqual(resultado, 2)

    def test_XI(self):
        resultado = roman_to_decimal('XI')
        self.assertEqual(resultado, 11)
        
    def test_VIII(self):
        resultado = roman_to_decimal('VIII')
        self.assertEqual(resultado, 8)
        
    def test_MDC(self):
        resultado = roman_to_decimal('MDC')
        self.assertEqual(resultado, 1600)
                   
    def test_MMMMDC(self):
        resultado = roman_to_decimal('MMMDC')
        self.assertEqual(resultado, 3600)           
    

if __name__ == '__main__':
    unittest.main()