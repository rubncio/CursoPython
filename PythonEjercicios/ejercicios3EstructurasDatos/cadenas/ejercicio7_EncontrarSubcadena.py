"""ide una frase y una palabra.
Indica si la palabra aparece en la frase y en qué posición."""
def encontrarPalabra(frase, palabra):
    return(str(frase).find(palabra)+1)


if(__name__=="__main__"):
    frase=input("Digame una frase por favor: ")
    palabra=input("Digame una palabra a encontrar por favor: ")
    indice=encontrarPalabra(frase, palabra)
    if indice>0:
        print(f"su palabra \"{palabra}\" se ha encontrado en la posición {indice}" )
    else:
        print(f"no se ha encontrado su palabra" )