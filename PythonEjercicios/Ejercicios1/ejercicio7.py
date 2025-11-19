import math
import time
"""Escoge uno de los siguientes ejercicios y haz un script con el programa.
Temporizador simple:
Crea un programa que muestre “3... 2... 1...” con pausas de un segundo entre cada número
usando time.sleep() y luego imprima “¡Listo!”.
Medir tiempo de escritura:
Mide cuánto tarda el usuario en escribir su nombre.
Guarda el tiempo antes y después de la entrada con time.time() y muestra la diferencia."""

print("escriba su nombre en: ")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
tiempoInicio=time.time()
nombre=input("¡YA!\n")
tiempoFinal=time.time()
time.sleep(0.5)
print(f"Enhorabuena {nombre}, tu tiempo de escritura ha sido de {round(tiempoFinal-tiempoInicio, 2)} segundos")