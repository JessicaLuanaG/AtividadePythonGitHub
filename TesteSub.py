def retorna_subtração(num1,num2):
    return num1-num2

import unittest

class testRetornaSubtração(unittest.TestCase):
    def test_retorna_subtração_vazia(self):
        self.assertEqual(retorna_subtração(2,2),0)
        
    def test_subtraçao(self):
        self.assertEqual(retorna_subtração(11, 6), 5)
    
    def test_subtraçao_negativa(self):
        self.assertEqual(retorna_subtração(-11, 6), -17)    
        
    def test_subtraçao_com_tres_numeros(self):
        self.assertEqual(retorna_subtração( 6, 4), 2)     
        
    def test_subtraçao_com_tres_numeros_negativos(self):
        self.assertEqual(retorna_subtração(-11, -6,), -5)

if __name__ == '__main__':
    unittest.main()       