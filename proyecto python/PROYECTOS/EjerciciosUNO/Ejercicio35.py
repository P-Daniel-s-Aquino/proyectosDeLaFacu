+"""Encriptar un mensaje usando el método de "la cifra del césar", 
que consiste en correr cada letra -considerando la posición de cada una en el 
alfabeto- una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, 
la palabra "HOLA" se transforma en "JQNC". Si el alfabeto termina antes de poder correr 
la cantidad de lugares necesarios, se vuelve a comenzar desde la letra "a"."""
def cifrarMensaje(mensaje, desplazamiento):
    mensajeCifrado = ""
    for letra in mensaje:
        if letra.isalpha():  # Verifica si es una letra
            asciiLetra = ord(letra)  # Obtiene el valor ASCII de la letra
            if letra.isupper():  # Para letras mayúsculas
                asciiLetra += desplazamiento
                if asciiLetra > ord('Z'):  # Si sobrepasa 'Z', vuelve al inicio
                    asciiLetra -= 26
            elif letra.islower():  # Para letras minúsculas
                asciiLetra += desplazamiento
                if asciiLetra > ord('z'):  # Si sobrepasa 'z', vuelve al inicio
                    asciiLetra -= 26
            mensajeCifrado += chr(asciiLetra)  # Convierte de nuevo a letra
        else:
            mensajeCifrado += letra  # Mantiene los caracteres no alfabéticos
    return mensajeCifrado


# Bucle que sigue pidiendo mensaje hasta que se ingrese una cadena vacía
while True:
    mensaje = input("Ingrese el mensaje que desea cifrar (o presione Enter para salir): \n")
    
    # Si el mensaje es una cadena vacía, se sale del bucle
    if mensaje == "":
        print("Saliendo del programa...")
        break
    
    desplazamiento = int(input("Ingrese un número entero para el desplazamiento del mensaje: \n"))
    
    # Cifrar el mensaje
    mensajeCifrado = cifrarMensaje(mensaje, desplazamiento)
    
    # Mostrar el resultado
    print("El mensaje cifrado es:", mensajeCifrado)

