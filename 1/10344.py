#Arena Out Of 23
from sys import stdin

def funcion(numeros, x, suma):
    if len(numeros) == x:
        return suma
    else:
        if funcion(numeros, x+1, suma+numeros[x]) == 23:
            return 23
        elif funcion(numeros, x+1, suma-numeros[x]) == 23:
            return 23
        elif funcion(numeros, x+1, suma*numeros[x]) == 23:
            return 23
        else:
            return 0

def main():
    lista = stdin.readline().strip().split()
    numeros = list(map(int,lista))

    suma = numeros[0]
    x = 1
    if funcion(numeros, x, suma) == 23:
        print("Possible")
    else:
        print("Impossible")
main()
