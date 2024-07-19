def retorna_subtração(lista):
    if len(lista) == 0:
        return "0"
    return sum(lista)

import unittest

class testRetornaSubtração(unittest.TestCase):
    def test_retorna_subtração_vazia(self):
        self.assertEqual(retorna_subtração([]), "0")
        
    def test_subtraçao(self):
        self.assertEqual(retorna_subtração([11, 6], 5))
    
    def test_subtraçao_negativa(self):
        self.assertEqual(retorna_subtração([-11, 6], -17))    
        
    def test_subtraçao_com_tres_numeros(self):
        self.assertEqual(retorna_subtração([11, 6, 4], 1))     
        
    def test_subtraçao_com_tres_numeros_negativos(self):
        self.assertEqual(retorna_subtração([-11, -6, -4], -1))

if __name__ == '__main__':
    unittest.main()       