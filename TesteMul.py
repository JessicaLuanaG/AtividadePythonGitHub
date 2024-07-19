def retorna_multiplicação(lista):
    if len(lista) == 0:
        return "0"
    return sum(lista)

import unittest

class testRetornaMultiplicação(unittest.TestCase):
    def test_retorna_multiplicaçaõ_vazia(self):
        self.assertEqual(retorna_multiplicação([]), "0")
        
    def test_multiplicaçaõ(self):
        self.assertEqual(retorna_multiplicaçãoo([5, 3], 15))
    
    def test_multiplicaçaõ_negativa(self):
        self.assertEqual(retorna_multiplicação([-5, 3], -15))    
        
    def test_multiplicaçaõ_com_tres_numeros(self):
        self.assertEqual(retorna_multiplicaçãoção([5, 3, 2], 30))     

    def test_multiplicaçaõ_com_tres_numeros_negativos(self):
        self.assertEqual(retorna_multiplicaçãoção([-5, -3, -2], -30))

if __name__ == '__main__':
    unittest.main()