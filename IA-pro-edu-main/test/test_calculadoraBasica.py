import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'SRC'))
from app.calculator import calcular


class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(calcular(5, 3, "+"), 8)

    def test_resta(self):
        self.assertEqual(calcular(5, 3, "-"), 2)

    def test_multiplicacion(self):
        self.assertEqual(calcular(5, 3, "*"), 15)

    def test_division(self):
        self.assertEqual(calcular(6, 3, "/"), 2)

    def test_division_por_cero(self):
        self.assertEqual(calcular(5, 0, "/"), "Error: No se puede dividir entre 0")

    def test_operacion_invalida(self):
        self.assertEqual(calcular(5, 3, "%"), "Operación no válida")


if __name__ == "__main__":
    unittest.main()
