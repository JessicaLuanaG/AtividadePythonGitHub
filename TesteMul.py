def retorna_multiplicação(num1,num2):
    return num1*num2

import unittest

class testRetornaMultiplicação(unittest.TestCase):
    def test_retorna_multiplicaçaõ_vazia(self):
        self.assertEqual(retorna_multiplicação(5,1), 5)
        
    def test_multiplicaçaõ(self):
        self.assertEqual(retorna_multiplicação(5, 3), 15)
    
    def test_multiplicaçaõ_negativa(self):
        self.assertEqual(retorna_multiplicação(-5, 3), -15)    
        
    def test_multiplicaçaõ_com_tres_numeros(self):
        self.assertEqual(retorna_multiplicação(5, 3), 15)     

    def test_multiplicaçaõ_com_tres_numeros_negativos(self):
        self.assertEqual(retorna_multiplicação(-5, -2), 10)

if __name__ == '__main__':
    unittest.main()