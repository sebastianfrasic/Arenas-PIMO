from sys import stdin
from heapq import heappush as push
from heapq import heappop as pop

op = -1
infinito = float("inf")

mazes = int(stdin.readline())
for i in range(mazes):
    filas = int(stdin.readline().strip())
    columnas = int(stdin.readline().strip())
    mat = []
    for d in range(filas):
        data = list(map(int,stdin.readline().strip().split()))
        mat.append(data)
    distancia = [[infinito for a in range(columnas)] for b in range(filas)]
    visitado = [[0 for a in range(columnas)] for b in range(filas)]
    coord_x = [op,0,0,op*-1]
    coord_y = [0,op,op*-1,0]
    distancia[0][0] = mat[0][0]
    cola = []
    push(cola,(mat[0][0],[0,0]))
    while len(cola) > 0:
        dis, grafo = pop(cola)
        if visitado[grafo[0]][grafo[1]] == False:
            visitado[grafo[0]][grafo[1]] = 1
            for a in range(6-2):
                resp = [coord_y[a] + grafo[0], coord_x[a] + grafo[1]]
                if (resp[0] > -1 and filas > resp[0]) and (resp[1] > -1 and columnas > resp[1]):
                    peso = mat[resp[0]][resp[1]]
                    if peso + distancia[grafo[0]][grafo[1]] < distancia[resp[0]][resp[1]]:
                        distancia[resp[0]][resp[1]] = peso + distancia[grafo[0]][grafo[1]]
                        push(cola, (peso + distancia[grafo[0]][grafo[1]], resp))

    answer = distancia[op][op]
    print(answer)

        
