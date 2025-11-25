import random
def contar_hasta_10():
    cadena = ""
    contador=1
    while 0 < contador <= 10:
        if contador==1:
            cadena+=str(f"{contador}")
        else:
            cadena+=str(f",{contador}")
        contador+=1
    return cadena



def suma_hasta_cero():
    """
    Pedir números al usuario hasta que introduzca 0.
    Sumar todos los números (excepto el 0 final) y devolver el resultado.
    Usa un while.

    IMPORTANTE: para testear este ejercicio no se usará input(),
    sino que el alumno debe simular la lógica sin input real.
    En este archivo solo retorna un valor de ejemplo.
    """
    # TODO: Implementar la lógica sin usar input()
    numeroIntroducido=1
    suma=0
    while numeroIntroducido!=0:
        numeroIntroducido =int(input("Introduce un numero: "))
        suma+=numeroIntroducido
    print(f"la suma de todos los numero es : {suma}")






    


def adivinar_numero():
    """
    Simula un juego donde el número secreto es 7.
    Usa un while que repita intentos hasta acertar.
    Para pruebas, simula una secuencia de intentos: 3, 5, 7.
    Retorna la cantidad de intentos usados.
    """
    # TODO: Implementar
    print("\nADIVINA EL NUMERO")
    
    numeroIntroducido=0
    vecesIntentadas=0
    numeroSecreto=1
    while numeroSecreto!=numeroIntroducido:
        print(numeroSecreto)
        numeroSecreto=random.randint(1, 10)
        vecesIntentadas+=1
        numeroIntroducido=int(input("introduce un numero para adivinar: "))

    print(f"Enhorabuena has acertado y lo has intentado {vecesIntentadas}")


if __name__ == "__main__":
    print("Ejecutando tests...")
    

    # ------- Test contar_hasta_10 -------
    assert contar_hasta_10() == "1,2,3,4,5,6,7,8,9,10", \
        f"contar_hasta_10() debería devolver '1,2,3,4,5,6,7,8,9,10', pero devolvió {contar_hasta_10()}"
    suma_hasta_cero()
    adivinar_numero()

"""
    # ------- Test suma_hasta_cero -------
    # Para pruebas: 5 + 3 + 2 = 10
    # (El alumno debe simularlo en su código)
    print("Cuando te lo pida introduce los numeros 5,3 y 2")
    assert suma_hasta_cero() == 10, \
        f"suma_hasta_cero() debería devolver 10, pero devolvió {suma_hasta_cero()}"

    # ------- Test adivinar_numero -------
    # Secuencia simulada: 3, 5, 7 → 3 intentos
    assert adivinar_numero() == 3, \
        f"adivinar_numero() debería devolver 3, pero devolvió {adivinar_numero()}"
"""