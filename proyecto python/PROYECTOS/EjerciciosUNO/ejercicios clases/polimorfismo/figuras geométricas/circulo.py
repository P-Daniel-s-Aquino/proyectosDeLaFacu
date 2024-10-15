from figuras_geometricas import Figuras
import math

class Circulo(Figuras):
    def __init__(self, radio):
        super().__init__("Circulo")
        self.radio = radio
    
    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return area
    
    def __str__(self):
        return f"Figura: {self.nombre}, Radio: {self.radio}, Área: {self.calcular_area()}"
        