# Archivo con los tests unitarios

import unittest
from basicfunction import BasicFunction

class TestBasicFunction(unittest.TestCase):
    def setUp(self):
        # Se define en esta clase una instancia de la clase a testear
        self.func = BasicFunction()

    def test1(self):
        # Para probar si la inicializacion de valores funciona
        self.assertEqual(self.func.state, 0)
    
    def test2(self):
        # Para probar si incrementar un valor funciona
        self.func.incrementState()
        self.assertEqual(self.func.state, 1)

    def test3(self):
        # Para probar si el clear funciona
        self.func.incrementState()
        self.func.incrementState()
        self.func.clearState()
        self.assertEqual(self.func.state, 0)

if __name__ == '__main__':
    unittest.main()