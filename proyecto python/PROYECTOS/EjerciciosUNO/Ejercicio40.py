"""Dado un conjunto de número enteros mayores o iguales a 0 y menores 
que 100 determinar e informar cuántas veces aparece cada uno. 
El conjunto finaliza con la llegada de un valor negativo"""

def contar_apariciones():
  conteo = {}
  
  while True:
    numero = int(input("Introduce un numero (negativo para finalizar): "))
    
    if numero < 0:
      break 
    elif 0 <= numero < 100:
      if numero in conteo:
        conteo[numero] += 1
      else: 
        conteo[numero] = 1
    else:
      print(f"El numero: {numero} esta fuera del rango. (debe estar entre 0 y 99)")
  for numero, veces in sorted(conteo.items()):
    print(f"El numero {numero} aparecio {veces} veces.")

contar_apariciones()