import unittest 
from circulo import Circulo
from triangulo import Triangulo
from rectangulo import Rectangulo

class TestFigurasGeometricas(unittest.TestCase):

    def test_calcular_area_circulo(self):
        circulo = Circulo(5)
        area = circulo.calcular_area()
        self.assertAlmostEqual(area, 78.539816, places = 3)

    def test_calcular_area_triangulo(self):
        triangulo = Triangulo(4, 3)
        area = triangulo.calcular_area()
        self.assertEqual(area, 6)

    def test_calcular_area_rectangulo(self):
        rectangulo = Rectangulo(6, 2)
        area = rectangulo.calcular_area()
        self.assertEqual(area, 12)

    def test_str_circulo(self):
        circulo = Circulo(5)
        self.assertEqual(str(circulo), f"Figura: Circulo, Radio: 5, Área: {circulo.calcular_area()}")

    def test_str_triangulo(self):
        triangulo = Triangulo(4, 3)
        self.assertEqual(str(triangulo), f"Figura: Triángulo, Base: 4, Altura: 3, Área: 6.0")

    def test_str_rectangulo(self):
        rectangulo = Rectangulo(6, 2)
        self.assertEqual(str(rectangulo), f"Figura: Rectángulo, Base: 6, Altura: 2, Área: 12")

if __name__ == '__main__':
    unittest.main()