from sys import stdin
from heapq import heappush as push
from heapq import heappop as pop


infinito = float("inf")

def Relajamiento(grafo, resp, peso, d, cola):
    if peso + d[grafo] < d[resp]:
        d[resp] = peso + d[grafo]
        push(cola,(peso + d[grafo], resp))
        
def main():
    casos = int(stdin.readline())
    for i in range(casos):
        data = [int(x) for x in stdin.readline().split()]
        matriz = [[] for k in range(data[0])]
        for j in range(data[1]):
            conexion = [int(x) for x in stdin.readline().split()]
            matriz[conexion[1]].append((conexion[0],conexion[2]))
            matriz[conexion[0]].append((conexion[1],conexion[2]))   
        d = [infinito for k in range(data[0])]
        d[data[2]] = 0
        cola = []
        push(cola,(0, data[2]))
        while len(cola) != 0:
            a, grafo = pop(cola)
            if d[grafo] != infinito:
                for resp, peso in matriz[grafo]:
                    Relajamiento(grafo, resp, peso, d, cola)
        if infinito == d[data[3]]:
            print("Case #" + str(i+1) + ": unreachable")
        else:
            print("Case #" + str(i+1) + ": " + str(d[data[3]]))
            
main()

            
