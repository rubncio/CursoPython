def añadirEspacio(numEspacios):
    contador=0
    espacios=""
    while(contador<numEspacios):
        espacios+=" "
        contador+=1

    return espacios

def añadirCaracteres(numeroC):
    contador=0
    caracteres=""
    while(contador<numeroC):
        caracteres+="#"
        contador+=1

    return caracteres

contadorEspacios=5
numCaracteres=1
while(contadorEspacios>=0):
    linea=f"{añadirEspacio(contadorEspacios)}{añadirCaracteres(numCaracteres)}"
    print(linea)
    contadorEspacios-=1
    numCaracteres+=2
