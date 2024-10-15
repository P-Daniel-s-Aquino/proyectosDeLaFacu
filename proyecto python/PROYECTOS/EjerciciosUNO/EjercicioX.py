"""Escribir una función que reciba dos arreglos a1 y a2  y devuelva otro arreglo 
como resultado de poner uno a continuacion del otro. Por ejemplo:
a1 = [-5, 0, 0, 1, 5]
a2 = [-10, 0, 7]
resultado = [-5, 0, 0, 1, 5, -10, 0, 7]
"""

def concatenar_arreglo(a1, a2):
  a3 = a1 + a2
  return a3

a1 = [-5, 0, 0, 1, 5]
a2 = [-10, 0, 7]

concatenado = concatenar_arreglo(a1, a2)
print(concatenado)


