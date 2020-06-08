import unittest
from unittest.mock import patch

def saludar():
    name = input('Hola, como te llamas?')
    ape= input('Apellido? ')
    return 'Como va %s %s!!!' % (name,ape)

class TestSaludar(unittest.TestCase):
    def test_saludar(self):
        with patch('builtins.input', side_effects=["Gabriel","Perez"]):
            self.assertEqual(saludar(), 'Como va Gabriel Perez!!!')

if __name__ == '__main__':
    unittest.main()