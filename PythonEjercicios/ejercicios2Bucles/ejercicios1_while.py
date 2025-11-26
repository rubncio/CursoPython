import random
import time
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


#SIN INPUT
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

    numerosIntroducidos=[5,3,2,0]
    suma=0
    contador=0
    while contador<len(numerosIntroducidos):
        print("Introduce un numero")
        numero=numerosIntroducidos[contador]
        #Se para la ejecucion 1s para simular la entrada de datos. 
        time.sleep(1)
        print(f"Numero Introducido: {numero}")
        if numero==0:break
        suma+=numero
        contador+=1
    print(f"la suma de todos los numero es : {suma}")
    return suma

# def suma_hasta_cero_con_input():
#     """
#     Pedir números al usuario hasta que introduzca 0.
#     Sumar todos los números (excepto el 0 final) y devolver el resultado.
#     Usa un while.

#     IMPORTANTE: para testear este ejercicio no se usará input(),
#     sino que el alumno debe simular la lógica sin input real.
#     En este archivo solo retorna un valor de ejemplo.
#     """
#     # TODO: Implementar la lógica sin usar input()
#     numeroIntroducido=1
#     suma=0
#     while numeroIntroducido!=0:
#         numeroIntroducido =int(input("Introduce un numero: "))
#         suma+=numeroIntroducido
#     print(f"la suma de todos los numero es : {suma}")

    

#SIN INPUT
def adivinar_numero():
    """
    Simula un juego donde el número secreto es 7.
    Usa un while que repita intentos hasta acertar.
    Para pruebas, simula una secuencia de intentos: 3, 5, 7.
    Retorna la cantidad de intentos usados.
    """
    # TODO: Implementar
    print("\nADIVINA EL NUMERO")
    
    numerosIntroducidos=[3,5,7]
    vecesIntentadas=1
    numeroSecreto=7
    contador=0
    
    while True:
        print("introduce un numero")
        numeroIntroducido=numerosIntroducidos[contador]
        time.sleep(1)
        print(f"numero introducido: {numeroIntroducido}")
        if numeroSecreto==numerosIntroducidos[contador]:break
        contador+=1
        vecesIntentadas+=1
    print(f"Enhorabuena has acertado y lo has intentado {vecesIntentadas} veces.")
    return vecesIntentadas

# def adivinar_numero_con_input():
#     """
#     Simula un juego donde el número secreto es 7.
#     Usa un while que repita intentos hasta acertar.
#     Para pruebas, simula una secuencia de intentos: 3, 5, 7.
#     Retorna la cantidad de intentos usados.
#     """
#     # TODO: Implementar
#     print("\nADIVINA EL NUMERO")
    
#     numeroIntroducido=0
#     vecesIntentadas=0
#     numeroSecreto=1
#     while numeroSecreto!=numeroIntroducido:
#         
#         numeroSecreto=random.randint(1, 10)
#         vecesIntentadas+=1
#         numeroIntroducido=int(input("introduce un numero para adivinar: "))

#     print(f"Enhorabuena has acertado y lo has intentado {vecesIntentadas} veces.")


if __name__ == "__main__":
    print("Ejecutando tests...")
    

    # ------- Test contar_hasta_10 -------
    assert contar_hasta_10() == "1,2,3,4,5,6,7,8,9,10", \
        f"contar_hasta_10() debería devolver '1,2,3,4,5,6,7,8,9,10', pero devolvió {contar_hasta_10()}"
    print(contar_hasta_10())
    # suma_hasta_cero_con_input()
    # adivinar_numero_con_input()


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
