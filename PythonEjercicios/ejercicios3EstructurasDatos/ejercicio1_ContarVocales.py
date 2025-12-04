"""Pide al usuario una cadena y muestra cuántas vocales contiene (a, e, i, o, u)."""
def contarVocales(cadena):
    vocales="aáeéiíoóuú"
    vocalesArray=[vocal for vocal in str(cadena).lower() if vocal in vocales]
    salida=f"Su frase contiene {len(vocalesArray)} vocales siendo las siguientes categorias: A:{vocalesArray.count('a')+vocalesArray.count('á')}, E:{vocalesArray.count('e')+vocalesArray.count('é')}, I:{vocalesArray.count('i')+vocalesArray.count('í')}, O:{vocalesArray.count('o')+vocalesArray.count('ó')}, U:{vocalesArray.count('u')+vocalesArray.count('ú')}"
    return salida
if(__name__=="__main__"):
    cadenaIntroducida=input("Introduzca una frase cualquiera por favor: ")
    salida = contarVocales(cadenaIntroducida)
    print(salida)