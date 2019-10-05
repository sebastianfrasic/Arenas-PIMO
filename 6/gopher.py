from sys import stdin
import math
from collections import deque

"""Programa hecho por Juan Sebastián Gómez y Juan Sebastián Frásica"""

def edmonds_karp(C, source, sink):
    n = len(C)
    """Se crea una matriz igual al grafo con flujo 0"""
    F = [[0] * n for i in range(n)]
    while True:
        """Se busca un camino hasta el Target grande"""
        path = bfs(C, F, source, sink)
        """Si no encuentra camino cierra el ciclo"""
        if not path:
            break
        """Para todo el camino que encontró busca el flujo mas pequeño."""
        flow = min(C[u][v] - F[u][v] for u,v in path)
        """Para todo el camino que encontro actualiza con el flujo mas pequeño."""
        for u,v in path:
            F[u][v] += flow
    return sum(F[source][i] for i in range(n))

def bfs(C, F, source, sink):
    """Paths va a guardar el camino por el cual llegue a cada nodo """
    queue = [source]
    paths = {source: []}
    while queue:
        u = queue.pop(0)
        for v in range(len(C)):
            """si el flujo que pasa es mayor a 0 y no he visitado v en esta búsqueda avanza"""
            if C[u][v] - F[u][v] > 0 and v not in paths:
                """El camino hasta V es el camino hasta U mas (u,v)"""
                paths[v] = paths[u] + [(u,v)]
                """Si llegue al Target grande retorno el camino por el cual llegue"""
                if v == sink:
                    return paths[v]
                queue.append(v)
    """Si no encuentro camino None"""
    return None

def main():
    """El algoritmo de Edmun karp es una implementación de MAX-FLOW
(busca que exista un camino de la source al target y para hallar esa
ruta hace un bfs)"""
    n= [int(x) for x in stdin.readline().strip().split()]
    while n:
        m = n[1]
        s = n[2]
        v = n[3]
        n = n[0]
        matriz = [[0 for i in range (n+m+2)]for j in range(n+m+2)]
        gophers = []
        holes = []
        for i in range(n):
            gophers.append(list(map(float,stdin.readline().split())))
            matriz[0][i+1] = 1
        for i in range(m):
            holes.append(list(map(float,stdin.readline().split())))
            matriz[n+1+i][-1] = 1
        maximo = s*v
        for i in range(n):
            for j in range(m):
                dx =gophers[i][0]-holes[j][0]
                dy = gophers[i][1]-holes[j][1]
                dis = math.sqrt((dy**2)+(dx**2))
                if dis <= maximo:
                    matriz[i+1][j+n+1] = 1
        a = edmonds_karp(matriz, 0, n+m+1)
        print(n-a)
        n = [int(x) for x in stdin.readline().strip().split()]
        
main()
