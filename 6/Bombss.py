from sys import stdin
import collections

def Deep_Search(x, matriz, n, m):
    mat_visitados =[[0 for i in range(m)] for j in range(n)]
    distancia = [[0 for i in range(m)]for j in range(n)]
    mat_visitados[x[0]][x[1]] = 1
    distancia[x[0]][x[1]] = 0
    cola = collections.deque()
    cola.append(x)
    coord_x = [1-2,3-3,2-2,1]
    coord_y = [0,-1,1,0]
    while len(cola) > 0:
        grafo_u = cola.popleft()
        for i in range(5-1):
            resp = [coord_y[i] + grafo_u[0], coord_x[i] + grafo_u[1]]
            if (resp[0] > -1 and n > resp[0]) and (resp[1] > -1 and m > resp[1]) and (matriz[resp[0]][resp[1]] == True):
                if mat_visitados[resp[0]][resp[1]] == False:
                    mat_visitados[resp[0]][resp[1]] = 1
                    distancia[resp[0]][resp[1]] = distancia[grafo_u[0]][grafo_u[1]] + 1
                    cola.append(resp)
    return distancia 


def main():
    n, m = [int(x) for x in stdin.readline().strip().split()]
    while n != 0 and m != 0:
        matriz  = [[1 for i in range(m)] for j in range(n)]
        bomba = int(stdin.readline().strip())
        for i in range(bomba):
            line = [int(x) for x in stdin.readline().strip().split()]
            for j in range(line[1]):
                matriz[line[0]][line[j+2]] = 0
        inicial = [int(x) for x in stdin.readline().strip().split()]
        final = [int(x) for x in stdin.readline().strip().split()]
        print(Deep_Search(inicial, matriz, n, m)[final[0]][final[1]])
        n, m = [int(x) for x in stdin.readline().strip().split()]
main()
