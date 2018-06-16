# Archivo con los tests unitarios

import unittest
from test_clase.liquidacion import Liquidacion

class TestLiquidacion(unittest.TestCase):
    def setUp(self):
        # Se define en esta clase una instancia de la clase a testear
        self.liq = Liquidacion()

    def test1(self):
        # Para probar si la inicializacion de valores funciona
        self.assertEqual(self.liq.valorHora, 250)
        self.assertEqual(self.liq.pctBonificacion, 8)
        self.assertEqual(self.liq.pctRetenciones, 11)
        self.assertEqual(self.liq.pctObraSocial, 3)
    
    def test2(self):
        # Para probar si el calculo del basico funciona
        self.assertEqual(self.liq.calcularSueldoBasico(10), 2500)

    def test3(self):
        # Para probar si el calculo del bruto funciona
        self.assertEqual(self.liq.calcularSueldoBruto(2500,3),2950)

    def test4(self):
        # Para probar si el calculo del neto funciona
        self.assertEqual(self.liq.calcularSueldoNeto(2950),2537)

    def testIntegracion1(self):
        # Para probar toda la clase completa ~test de integracion
        self.assertEqual(self.liq.calcularSueldoEmpleado(20,5),5504)
                    
if __name__ == '__main__':
    unittest.main()