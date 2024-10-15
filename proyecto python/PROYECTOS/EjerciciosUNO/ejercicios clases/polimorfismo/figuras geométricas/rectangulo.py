from figuras_geometricas import Figuras

class Rectangulo(Figuras):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        area = self.base * self.altura
        return area
    
    def __str__(self):
        return f"Figura: {self.nombre}, Base: {self.base}, Altura: {self.altura}, Área: {self.calcular_area()}"
