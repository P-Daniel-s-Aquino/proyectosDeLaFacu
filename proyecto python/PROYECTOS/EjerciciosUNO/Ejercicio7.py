"""Leer un valor numérico que representa un día de la semana. 
Se pide mostrar por pantalla el nombre del día considerando que 
el lunes es el día 1, el martes es el día 2 y así, sucesivamente"""

def pedir_dia():
    while True:
        try:
            # Pedir al usuario que ingrese un número del 1 al 7
            entrada = input("Ingrese un día de la semana (1-7): ")
            
            # Convertir la entrada a entero
            dia = int(entrada)
            
            # Verificar si el número está en el rango permitido
            if 1 <= dia <= 7:
                return dia
            else:
                print("Ingrese un valor válido (entre 1 y 7).")
        
        except ValueError:
            # Manejar el caso en el que la conversión a entero falla
            print("Por favor, ingrese un número válido.")

while True:
    # Pedir al usuario que ingrese un día de la semana
    dia_seleccionado = pedir_dia()
    
    # Utilizar la estructura de match para mostrar el nombre del día
    match dia_seleccionado:
        case 1:
            print("Lunes")
        case 2:
            print("Martes")
        case 3:
            print("Miércoles")
        case 4:
            print("Jueves")
        case 5:
            print("Viernes")
        case 6:
            print("Sábado")
        case 7:
            print("Domingo")
            break
    
    # Solicitar al usuario que ingrese un nuevo día (sólo si el anterior fue válido)
    if input("Desea ingresar un nuevo día? (S/N): ").lower()!= "s":
        break

