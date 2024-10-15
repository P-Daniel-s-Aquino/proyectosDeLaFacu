"""Escribir una función que reciba un string y lo devuelva invertido. 
Por ejemplo: invertirCadena("Hola"),retorna "aloH". Reutilice la función 
implementada para decir si una palabra es o no, un palíndromo. 
esPalindromo("neuquen") devuelve true"""

def dar_vuelta(string):
    """Devuelve la cadena invertida."""
    return string[::-1]

def es_palindromo(string):
    """Verifica si una cadena es un palíndromo, ignorando mayúsculas y minúsculas."""
    # Convertir la cadena a minúsculas
    string = string.lower()
    # Comparar la cadena original con su versión invertida
    return string == dar_vuelta(string)

# Solicitar la entrada del usuario
string = input("Ingrese una palabra: ")

# Ejecutar la función y mostrar el resultado
print(f"¿La palabra '{string}' es un palíndromo? {es_palindromo(string)}")

if len(string) % 2 == 0:
    print(f"La palabra '{string}' no es un palindromo")

# Ejecutar la función con ejemplos
print(f"¿La palabra 'neuquen' es un palíndromo? {es_palindromo('neuquen')}") # Devuelve True
print(f"¿La palabra 'radar' es un palíndromo? {es_palindromo('radar')}")   # Devuelve True
print(f"¿La palabra 'hola' es un palíndromo? {es_palindromo('hola')}")     # Devuelve False
