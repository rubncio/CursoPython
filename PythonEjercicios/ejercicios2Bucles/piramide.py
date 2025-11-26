# def añadirEspacio(numEspacios):
#     contador=0
#     espacios=""
#     while(contador<numEspacios):
#         espacios+=" "
#         contador+=1

#     return espacios

# def añadirCaracteres(numeroC):
#     contador=0
#     caracteres=""
#     while(contador<numeroC):
#         caracteres+="#"
#         contador+=1

#     return caracteres

# def añadir(numero, tipoCaracter):
#     lineaCaracteres=int(numero)*str(tipoCaracter)
#     return lineaCaracteres

def crearPiramide(numeroFilas, tipoCaracter):
    filasRestantes=numeroFilas
    numEspacios=filasRestantes-1
    numCaracteres=1
    while(filasRestantes>0):
        #linea=f"{añadir(numEspacios, ' ')}{añadir(numCaracteres, tipoCaracter)}"
        linea=int(numEspacios)*" "+int(numCaracteres)*str(tipoCaracter)

        print(linea)
        numEspacios-=1
        numCaracteres+=2
        filasRestantes-=1

if __name__=="__main__":
    numFilas=int(input("Indica de cuantas filas quieres la piramide: "))
    tipoCaracter=input("Indica que tipo de caracter quieres usar: ")
    crearPiramide(numFilas, tipoCaracter)
