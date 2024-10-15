"""En el método main de la clase TestInterface declarar un arreglo de N figuras (Interface). 
Las figuras pueden ser cuadrados, círculos y rectángulos. Todos responden al mensaje area.
Mostrar en consola el siguiente mensaje: "De un total de N figuras, el área total es de ..."""

from abc import ABCMeta, abstractmethod

class Figuras(metaclass = ABCMeta):
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod    
    def calcular_area(self) -> float:
        pass
    