"""metodos son una funcion dentro de una clase, determinando una accion o comportamiento"""

# class Matematica:
#     #self hace referencia a un objeto
#     def sumar(self):
#         self.numero1 = 2
#         self.numero2 = 3

# suma = Matematica()
# suma.sumar()
# print(suma.numero1 + suma.numero2)

# class Ropa:
#     def __init__(self):
#         self.marca = "Kloster"
#         self.talla = 'M'
#         self.color = "Rojo"     

# camisa = Ropa()
# print(camisa.marca)
# print(camisa.talla)
# print(camisa.color)

class Calculadora:
    def __init__(self, numero1, numero2):
        self.sumar = numero1 + numero2
        self.restar = numero1 - numero2
        self.multiplicar = numero1 * numero2
        self.dividir = numero1 / numero2

operacion = Calculadora(2, 3)
print(operacion.sumar)
print(operacion.restar)
print(operacion.multiplicar)
print(operacion.dividir)  