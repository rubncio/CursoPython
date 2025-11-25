import time


if __name__ == "__main__":
    n=0
    while n<1 or n>10:
        n=int(input("Diga un numero de 1 al 10: "))
    
    while n>0:
        print(f"¡¡{n}!!")
        n-=1
        time.sleep(1)
    

    