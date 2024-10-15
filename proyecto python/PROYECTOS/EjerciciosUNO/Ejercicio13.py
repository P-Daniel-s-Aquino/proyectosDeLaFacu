"""Se ingresa un valor numérico por consola, determinar
   e informar si se trata de un número primo o no"""
   
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    
    i = 5
    
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    
    return True

while True:
    numero = int(input("Ingrese un número: "))
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

    if input("Desea ingresar otro numero? (s/n) ").lower() != "s":
        break