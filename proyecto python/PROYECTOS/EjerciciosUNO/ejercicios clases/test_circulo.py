import unittest
import math
from circulo import Circulo

class TestCirculo(unittest.TestCase):
    def setUp(self):
        self.circulo = Circulo(5)
        
    def test_obtener_radio(self):
        self.assertEqual(self.circulo.obtener_radio(), 5)
        
    def test_obtener_diametro(self):
        self.assertEqual(self.circulo.obtener_diametro(), 10)
        
    def test_obtener_perimetro(self):
        self.assertAlmostEqual(self.circulo.obtener_perimetro(), 10 * math.pi, places=5)
   
    def test_obtener_area(self):
        self.assertAlmostEqual(self.circulo.obtener_area(), math.pi * 25, places=5)
        
    def test_cambiar_radio(self):
        self.circulo.cambiar_radio(10)
        self.assertEqual(self.circulo.obtener_radio(), 10)
        self.assertEqual(self.circulo.obtener_diametro(), 20)
        self.assertAlmostEqual(self.circulo.obtener_perimetro(), 20 * math.pi, places=5)
        self.assertAlmostEqual(self.circulo.obtener_area(), math.pi * 100, places=5)
        
if __name__ == "__main__":
    unittest.main()
