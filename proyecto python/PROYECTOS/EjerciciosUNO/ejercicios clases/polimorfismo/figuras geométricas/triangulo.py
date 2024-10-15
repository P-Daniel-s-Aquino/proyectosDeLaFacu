from figuras_geometricas import Figuras

class Triangulo(Figuras):
    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return area
    
    def __str__(self):
        return f"Figura: {self.nombre}, Base: {self.base}, Altura: {self.altura}, Área: {self.calcular_area()}"
