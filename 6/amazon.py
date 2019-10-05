from math import sqrt as raiz
from collections import deque
from sys import stdin
def BFS(ady,bol,pos):
    bol[pos] = True
    cola = deque()
    aux = len(ady[pos])
    for i in range(aux):
        cola.append(ady[pos].pop(0))
    while len(cola) != 0:
        nodo = cola.popleft()
        bol[nodo] = True
        aux = len(ady[nodo])
        for j in range(aux):
            cola.append(ady[nodo].pop(0))
    return bol
            
def main():
    while True:
        entero = int(stdin.readline().strip())
        ady = [[] for i in range(entero)]
        mascortas = [[] for i in range(entero)]
        distancia = [[] for i in range(entero)]
        if entero == 0:
            break
        coordenadas = [int(d) for d in stdin.readline().strip().split()]
        if entero == 1 or entero == 2 or entero == 3:
            print('All stations are reachable.')
        else:
            coordenadas = [coordenadas[i:i+2] for i in range(0,len(coordenadas),2)]
            for i in range(entero):
                for j in range(entero):
                    if i == j:
                        continue
                    xi = coordenadas[i][0]
                    yi = coordenadas[i][1]
                    xf = coordenadas[j][0]
                    yf = coordenadas[j][1]
                    distans = raiz((xf-xi)**2+(yf-yi)**2)
                    #print(distans)
                    distancia[i].append((distans,xf,yf,j))
                #print('.')
            nta = 0
            grafo = 0
            for i in distancia:
                i.sort()
                opc1=i[0][-1]
                opc2=i[1][-1]
                ady[grafo].append(opc1)
                ady[grafo].append(opc2)
                grafo +=1
            bol = [False for i in range(entero)]
            BFS(ady,bol,0)
            if sum(BFS(ady,bol,0)) != entero:
                print('There are stations that are unreachable.')
            else:
                print('All stations are reachable.')  
main()
