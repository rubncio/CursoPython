import os
"""Haz un script que ejecute estas acciones por pasos:
Directorio actual:
Muestra el directorio de trabajo actual con os.getcwd().
Crear carpeta:
Crea una nueva carpeta llamada "prueba_python" utilizando os.mkdir().
Listar archivos:
Muestra todos los archivos y carpetas en el directorio actual con os.listdir()"""

if(__name__=="__main__"):
    carpetaActual=os.getcwd()
    print(f"La carpeta de trabajo actual es {carpetaActual}")
    if(os.access(carpetaActual+"\prueba_python", os.F_OK)):
        print("el directorio prueba_python ya existe.")
    else:
        print("Creando carpeta prueba_python.")
        os.mkdir(carpetaActual+"\prueba_python")
        

    print(f"Mostrando listado: \n{os.listdir(carpetaActual)}")
