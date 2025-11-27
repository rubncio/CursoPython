def crearPiramide(numeroFilas, tipoCaracter):
    filasRestantes=int(numeroFilas)
    numEspacios=filasRestantes-1
    numCaracteres=1
    piramide=""
    while(filasRestantes>0):
        #linea=f"{añadir(numEspacios, ' ')}{añadir(numCaracteres, tipoCaracter)}"
        linea=numEspacios*" "+numCaracteres*str(tipoCaracter)

        piramide+=f"{linea}\n"
        numEspacios-=1
        numCaracteres+=2
        filasRestantes-=1
    return piramide

def crearCuadro(numeroFilas, tipoCaracter):
    filasRestantes=int(numeroFilas)
    numEspacios=filasRestantes-1
    numCaracteres=1
    piramide=""
    while(filasRestantes>0):
        #linea=f"{añadir(numEspacios, ' ')}{añadir(numCaracteres, tipoCaracter)}"
        linea=numEspacios*" "+numCaracteres*str(tipoCaracter)

        piramide+=f"{linea}\n"
        numEspacios-=1
        numCaracteres+=2
        filasRestantes-=1
    return piramide

if __name__=="__main__":
    numFilas=int(input("Indica de cuantas filas quieres la piramide: "))
    tipoCaracter=input("Indica que tipo de caracter quieres usar: ")
    piramide=crearPiramide(numFilas, tipoCaracter)
    print(piramide)
    cuadrado=crearCuadrado(numFilas, tipoCaracter)
    print(cuadrado)
    triangulo=crearTriangulo(numFilas, tipoCaracter)
    print(triangulo)
