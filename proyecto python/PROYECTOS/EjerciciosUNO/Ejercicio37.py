"""Escribir una función que reciba una cadena de caracteres muestre 
por pantalla la frecuencia de aparición de cada letra. Por ejemplo:
frecuencias("hola como estas..."); // debe mostrar por pantalla:"""

"""  
  a: 2
  c: 1
  e: 1
  h: 1
  l: 1
  m: 1
  o: 3
  s: 2
  t: 1  
"""

# def mostrar_frecuencia():  
#   cadena = input("Ingrese una cadena de caracteres: ")
#   print(f"a: {cadena.count("a")}")
#   print(f"c: {cadena.count("c")}")  
#   print(f"e: {cadena.count("e")}")
#   print(f"h: {cadena.count("h")}")
#   print(f"l: {cadena.count("l")}")
#   print(f"m: {cadena.count("m")}")
#   print(f"o: {cadena.count("o")}")
#   print(f"s: {cadena.count("s")}")
#   print(f"t: {cadena.count("t")}")
#   print(f": {cadena.count(" ")}")
  
# mostrar_frecuencia()
  
def mostrar_frecuencia(s):
  f = [0] * 26  # Crear una lista de 26 ceros, una para cada letra del alfabeto
    
  s = s.upper()  # Convertir toda la cadena a mayúsculas para uniformidad
  for l in s:
    if 'A' <= l <= 'Z':  # Verificar si el carácter es una letra mayúscula
      pos = ord(l) - ord('A')  # Calcular la posición en la lista
      f[pos] += 1
    
  for i in range(26):
    if f[i] != 0:
      print(chr(i + ord('A')), ":", f[i])  # Imprimir la letra y su frecuencia

# Solicitar al usuario una frase
palabra = input("Ingrese una frase: ")
mostrar_frecuencia(palabra)
