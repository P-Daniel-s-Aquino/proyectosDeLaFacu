class Tomate:
    def tipo(self):
        return "Es un vegetal"
    
    def color(self):
        return "De color rojo"
    
class Manzana:
    def tipo(self):
        return "Es una fruta"
    
    def color(self):
        return "De color verde"
    
    
def funcion(objeto):
    print(objeto.tipo())
    print(objeto.color())
    
tomate1 = Tomate()
funcion(tomate1)

manzana1 = Manzana()
funcion(manzana1)