"""Escribir una función que reciba dos arreglos a1 y a2, 
de enteros ordenados de menor a mayor e intercale los elementos
de los arreglos que recibe en un nuevo arreglo, tal que el arreglo 
resultante también esté ordenado. Por ejemplo:

a1 = [-5, 0, 0, 1, 5]
a2 = [-10, 0, 7]
resultado = [-10, -5, 0, 0, 0, 1, 5, 7]"""

def concatenar_arreglo(a1, a2):
  a3 = a1 + a2
  return a3

def ordenar_arreglo(concatenado):
    n = len(concatenado)
    for i in range(n):
        for j in range(0, n - i - 1):
            if concatenado[j] > concatenado[j + 1]:
                concatenado[j], concatenado[j + 1] = concatenado[j + 1], concatenado[j]
    return concatenado
# Listas
a1 = [-5, 0, 0, 1, 5]
a2 = [-10, 0, 7, 4, 6, -12]

concatenado = concatenar_arreglo(a1, a2)
print("Lista concatenada:", concatenado)

concatenado = ordenar_arreglo(concatenado)

print("Lista ordenada:", concatenado)
             