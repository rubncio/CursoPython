import random
"""Escoge uno de los siguientes ejercicios y haz un script con el programa.
Juego de adivinar el número:
Genera un número aleatorio entre 1 y 10 con random.randint() y pide al usuario que lo adivine.
Muestra un mensaje indicando si ha acertado o no.
Promedio de números aleatorios:
Genera tres números aleatorios entre 1 y 100 usando random.randint(), muéstralos por pantalla y
calcula su promedio.
Simulación de un dado:
Crea un programa que muestre un número aleatorio del 1 al 6 cada vez que se ejecuta, usando
random.randint()."""

if(__name__=="__main__"):
    numeroIndicado=int(input("Introduzca un numero para adivinar un numero del 1 al 10: "))
    numeroaleatorio=int(random.randrange(1,10))

    if(numeroaleatorio==numeroIndicado):
        print(f"Enhorabuena has acertado el numero con el {numeroaleatorio}")
    else:
        print(f"Ohh no has acertado el numero, ha salido el {numeroaleatorio}")