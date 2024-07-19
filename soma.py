def add(a:int, b:int) -> int:
    return a + b

import unittest

class teste_Add(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(3, 5), 8)
    
    def test_add_negative(self):
        self.assertEqual(add(-3, -5), -8)
    
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
    
    def test_add_large(self):
        self.assertEqual(add(1000000, 2000000), 3000000)

    def test_add_float(self):
        self.assertEqual(add(3.5, 5.2), 8.7)

if __name__ == '__main__':
    unittest.main()