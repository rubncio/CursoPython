"""Escribe un programa que invierta una cadena sin usar [::-1]."""
def invertirCadena(cadena):
    ultimoIndice=len(cadena)-1
    cadenaInvertida="".join([cadena[indice] for indice in range(ultimoIndice,-1, -1)])
    return cadenaInvertida

if __name__=="__main__":
    cadenaInput = input("Introduzca una cadena: ")
    print(f"Su cadena invertida es: \"{invertirCadena(cadenaInput)}\"")