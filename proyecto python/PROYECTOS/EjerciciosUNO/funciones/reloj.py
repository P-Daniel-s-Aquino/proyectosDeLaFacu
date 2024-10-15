"""Reloj que se actualiza cada segundo"""
import time
from datetime import datetime  

try:
    while True:
        ahora = datetime.now().strftime("%H:%M:%S")  # Usar datetime.now() para obtener la hora actual
        print(f"\rHora actual: {ahora}", end="")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nReloj interrumpido.")