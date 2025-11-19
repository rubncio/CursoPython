import math
"""Haz un script que ejecute estas acciones por pasos:
1.- Cálculo de raíz cuadrada:
Pide al usuario un número y muestra su raíz cuadrada usando la función math.sqrt().
2.- Área de un círculo:
Solicita al usuario el radio de un círculo y calcula su área utilizando math.pi y math.pow().
3.- Seno y coseno de un ángulo:
Pide al usuario un ángulo en grados y muestra su seno y coseno empleando math.sin() y
math.cos().
(Recuerda convertir los grados a radianes con math.radians().)"""
if(__name__=="__main__"):

    #1º
    numero=float(input("Introduzca un numero: "))
    raizcuadrada=math.sqrt(numero)
    print(f"La raiz cuadrada de tu numero {numero} es: {raizcuadrada}")

    #2º
    radio=float(input("Introduzca el radio de un circulo: "))
    areaCirculo=(math.pow(radio, 2)*math.pi)
    print(f"El area de tu circulo con un radio de {radio} es: {areaCirculo}")

    #3º
    angulo=float(input("Introduzca un angulo en grados: "))
    anguloradial=math.radians(angulo)
    seno=math.sin(anguloradial)
    coseno=math.cos(anguloradial)
    print(f"El seno y coseno con los grados {angulo} es: SENO={seno}, COSENO={coseno}")

