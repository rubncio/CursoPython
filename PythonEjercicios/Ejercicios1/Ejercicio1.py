import requests
'''haz un script que te pida tu nombre y te salude.
#A continuación, haz un script que te pida tu nombre y te salude, un color y un
objeto o lugar y genera una frase con las 3 variables.'''

def saludo():
    nombre, color, lugar=input("Di tu nombre: "),input("Di un color: "),input("Di un lugar: ")
    print(f"Hola {nombre}, que color tan bonito el {color}, y ya ni te digo el lugar {lugar}")
if(__name__=="__main__"):
    saludo()
