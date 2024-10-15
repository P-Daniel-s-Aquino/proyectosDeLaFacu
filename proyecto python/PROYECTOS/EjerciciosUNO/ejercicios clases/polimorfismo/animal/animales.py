#polimorfismo
class Animales:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def tipo_animal(self):
        pass
    
class Leon(Animales):
    def tipo_animal(self):
        return "Animal salvaje."
    
class Perro(Animales):
    def tipo_animal(self):
        return "Animal doméstico."

nuevo_animal = Leon("Simba")
print(nuevo_animal.tipo_animal()) 
    