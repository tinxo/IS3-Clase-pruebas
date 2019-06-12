# Archivo con los tests unitarios

import unittest
from test_clase.elecciones import leerArchivoNombres

class TestBasicFunction(unittest.TestCase):
    
    def test1(self):
        lista = ['Candidato1', 'Candidato2']
        self.assertListEqual(lista, leerArchivoNombres('candidatos.txt'))

    def test2(self):
        self.assertEqual(-1, leerArchivoNombres('error.txt'))

if __name__ == '__main__':
    unittest.main()