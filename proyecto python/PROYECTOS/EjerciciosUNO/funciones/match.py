numero = 2
match numero: # Coincidir números.
    case 1:
        print("El número es 1")
    case 2:
        print("El número es 2")
    case _: # El _ (guion bajo) se usa como default para el caso que no aplique a ninguno de los casos disponibles.
        print("El número no es 1 ni 2")
        
fruta = "UVA" # Coincidir cadenas.
match fruta.lower():
    case "manzana":
        print("La fruta es una manzana")
    case "pera":
        print("La fruta es una pera")
    case "uva":
        print("La fruta es una uva")
    case _:
        print("La fruta no es una manzana, pera, o uva")
        
lista = [1, 2, 3] # Coincidir listas.
match lista:
    case [1, 2, 3]:
        print("La lista contiene los números 1, 2, y 3")
    case [2, 2, 2]:
        print("La lista contiene los números 2, 2, y 2")    
    case _:
        print("La lista no contiene los números 1, 2, y 3")

persona = {"nombre" : "Juan", "edad" : 30} # Coincidir diccionarios.
match persona:
    case {"nombre" : "Daniel", "edad" : 30}:
        print("La persona es Juan de 30 años")
    case {"nombre" : "Ana", "edad" : 28}:
        print("La persona es Ana de 28 años")
    case _:
        print("La persona no es Juan ni Ana")

valor = 22
match valor:
    case x if 0 <= valor <= 10 : # Coincidir un patrón con guardia.
        print("El valor está entre 0 y 10")
    case x if x > 10 and x <= 20:
        print("El valor está entre 11 y 20")
    case x if x < 0:
        print("El valor es negativo")
    case _:
        print("El valor está fuera del rango")
