"""Dada una frase, reemplaza una palabra por otra usando replace().."""
import random


def reemplazaPalabras(cadena):
    palabras=[cadena for cadena in str(cadena).split(" ") if cadena!=""]
    indicePalabraOld=random.randint(1, len(palabras)-1)
    indicePalabraNew=random.randint(1, len(palabras)-1)
    cadenaSalida=str(cadena).replace(palabras[indicePalabraOld], palabras[indicePalabraNew])
    return cadenaSalida
if __name__=="__main__":
    cadenaInput=input("introduzca una frase por favor: ")
   
    print(reemplazaPalabras(cadenaInput))