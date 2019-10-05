from sys import stdin
from heapq import heappush as push
from heapq import heappop as pop

infinito = float("inf")

def Dijkstra():
    global matriz
    distance = [infinito for k in range(len(matriz))]
    visited = [0 for i in range(len(matriz))]
    distance[inicio] = 0
    cola = []
    push(cola, (distance[inicio], inicio))
    while len(cola) > 0:
        d, grafo = pop(cola)
        if 0 == visited[grafo]:
            for i in range(len(matriz[grafo])):
                if matriz[grafo][i] == "x":
                    continue
                else:
                    peso = int(matriz[grafo][i])
                    #Relajamiento
                    if peso + distance[grafo] < distance[i]:
                        distance[i] = peso + distance[grafo]
                        push(cola, (distance[i], i))
            visited[grafo] = 1
    return distance

def main ():
    global matriz, inicio
    inicio = 0
    n = stdin.readline().strip()
    while True:
        if n == '':
            break
        else:
            n = int(n)
            matriz = [[0 for i in range(n)] for i in range(n)]
            for i in range(1, n):
                data = stdin.readline().strip().split()
                for j in range (len(data)):
                    matriz[i][j] = data[j]
                    matriz[j][i] = data[j]
            resp = max(Dijkstra())           
            print (resp)
            n = stdin.readline().strip()
main()
