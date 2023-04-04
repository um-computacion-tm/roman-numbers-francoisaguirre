import unittest

def roman_to_decimal(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_num = 0
    for i in range(len(roman)):
        if i > 0 and roman_dict[roman[i]] > roman_dict[roman[i-1]]:
            decimal_num += roman_dict[roman[i]] - 2 * roman_dict[roman[i-1]]
        else:
            decimal_num += roman_dict[roman[i]]
    return decimal_num



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

if __name__ == '__main__':
    unittest.main()