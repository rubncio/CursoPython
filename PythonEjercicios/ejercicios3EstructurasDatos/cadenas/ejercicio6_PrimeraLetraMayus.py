"""Dada una frase desordenada como "hola mundo desde python", capitaliza la primera letra de cada palabra."""
def capitalizar(cadena):
    cadenaSalida=str().join([cadena.capitalize()+" " for cadena in str(cadena).split(" ") if cadena!=""])
    return cadenaSalida

if(__name__=="__main__"):
    cadenaCapitalizada=capitalizar(input("Introduzca una frase porfavor: "))
    print(f"su cadena capitalizada es \"{cadenaCapitalizada}\"")
