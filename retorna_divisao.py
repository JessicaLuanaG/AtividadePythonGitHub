def retorna_divisao(num1,num2):
    return num1/num2

import unittest

class testRetornaSoma(unittest.TestCase):
    def test_retorna_divisao_dois_pos(self):
        self.assertEqual(retorna_divisao(4,2), 2)
        
    def test_retorna_divisao_um_neg_um_pos(self):
        self.assertEqual(retorna_divisao(-5,5),-1)
        
    def test_retorna_divisao_quebrada(self):
        self.assertEqual(retorna_divisao(13,2), 6.5)
        
    def test_retorna_divisao_um_pos_um_negativo(self):
        self.assertEqual(retorna_divisao(-10,2), -5)
        
    def test_retorna_divisao_dois_negativos(self):
        self.assertEqual(retorna_divisao(-8,-4), 2)
        

if __name__ == '__main__':
    unittest.main()
