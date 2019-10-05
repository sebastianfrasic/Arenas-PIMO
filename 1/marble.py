#Where is the Marble?
from sys import stdin


def bbin(lista, elem):
    low = 0
    high = len(lista)
    resp = False
    while low < high:
        mid = low + ((high-low) //2)
        if lista[mid] != elem:
            if lista[mid] < elem:
                low = mid + 1
                
            else:
                high = mid
        else:
            return True
            
    return resp

def main():
    
    num_caso = 0
    n = list(map(int, stdin.readline().strip().split()))
    while n[0] and n[1] != 0:
        
        num_caso += 1
        print("CASE# " + str(num_caso) + ":")
        casos = n[0]
        numeros = n[1]
        lista_numeros = []
        for i in range(casos):
            numero = int(stdin.readline().strip())
            lista_numeros.append(numero)
        lista_numeros.sort()


        lista_buscados = []
        for j in range(numeros):
            buscado = int(stdin.readline().strip())
            lista_buscados.append(buscado)



        for k in range(len(lista_buscados)):

            busqueda = bbin(lista_numeros, lista_buscados[k])
            
            if busqueda == True:
                indice = lista_numeros.index(lista_buscados[k]) + 1
                print(str(lista_buscados[k]) + " found at " + str(indice))
            else:
                print(str(lista_buscados[k]) + " not found")
            
            

        n = list(map(int, stdin.readline().strip().split()))
    

main()
















            
