import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.calcular_datos()
    
    def calcular_datos(self):
        self.diametro = self.radio * 2
        self.perimetro = self.radio * 2 * math.pi
        self.area = math.pi * (self.radio ** 2)
        
    def obtener_radio(self):
        return self.radio
    
    def obtener_diametro(self):
        return self.diametro
    
    def obtener_perimetro(self):
        return self.perimetro
    
    def obtener_area(self):
        return self.area
    
    def cambiar_radio(self, nuevo_radio):
        self.radio = nuevo_radio
        self.calcular_datos() 