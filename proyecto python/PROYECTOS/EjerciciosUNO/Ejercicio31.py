"""Escribir una función que reciba un arreglo de enteros y devuelva la suma 
de los elementos que se encuentran en posiciones pares (incluido el elemento de la posición 0).
Por ejemplo: Dado el arreglo [1, 2, 13 ,4, 8, 6] => devuelve 22 (1+13+8)"""

def sumar_posiciones_par(arreglo):
    suma = 0
    for i in range(0, len(arreglo), 2):
        # if i % 2 == 0: en el caso de que se aumente en 1 
        suma += arreglo[i]
    return suma

arreglo = [1, 2, 13, 4, 8, 6]
print(sumar_posiciones_par(arreglo))
        