#Train Swapping

from sys import stdin

def burbuja(lista, tam):
    global cont
    cont = 0
    for i in range(tam):
        for j in range(i+1, tam):
            if lista[j] < lista[i]:
                lista[i], lista[j] = lista[j], lista[i]
                cont += 1
    return cont

def main():
    x = int(stdin.readline().strip())
    
    for i in range(x):
        y = int(stdin.readline().strip())
        lista = list(map(int, input().split()))
        veces = burbuja(lista, len(lista))
        print("Optimal train swapping takes " + str(veces) + " swaps.")
main()
            
    
