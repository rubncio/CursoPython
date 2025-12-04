def esPalindromo(palabra):
    palabraReves=palabra[::-1]
    return palabra==palabraReves

if __name__=="__main__":
    palabraInput=input("Introduzca una palabra palindroma: ")
    if(esPalindromo(palabraInput)):
        print(f"En efecto tu palabra \"{palabraInput}\" es palindroma, ere un fenomeno")
    else:
        print("esa palabra no es palindroma")