"""Solicita una frase y muestra cuántas palabras tiene"""
def contadorPalabras(cadena):
    palabrassin=[cadena for cadena in str(cadena).split(" ") if cadena!=""]
    print(palabrassin)
    return len(palabrassin)

if __name__ == "__main__":
    cadenaIntroducida = input("Introduzca una frase por favor: ")
    print(f"tu frase tiene {contadorPalabras(cadenaIntroducida)} palabras")