from sys import stdin
import heapq
from math import sqrt


def load_floats():
    line = stdin.readline().strip()
    return list(map(float, line.split()))

def load_case():
    stdin.readline().strip()
    numero = int(stdin.readline().strip())
    
    freckles = []
    for n in range(numero):
        freckles.append(tuple(load_floats()))
    
    return freckles


def distancia_puntos(a, b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


def min_tree(points):

    vertices = [0]
    edges = []    
    free = [(float("inf"), i+1, 0) for i, v in enumerate(points[1:])]
    
    def update_free(vertex):
        coordv = points[vertex]
        for i, f in enumerate(free):
            dist, fvertex, _ = f 
            coordf = points[fvertex]
            ndist = distancia_puntos(coordf, coordv)
            if ndist < dist:
                free[i] = (ndist, fvertex, vertex)

        heapq.heapify(free)

    update_free(0) 
   
    while free:
        dist, fvertex, vertex = heapq.heappop(free)
        vertices.append(fvertex)
        edges.append((vertex, fvertex))

        update_free(fvertex)
 
    return vertices, edges
  


def main():
    
    casos = int(stdin.readline().strip())

    for i in range(casos):
        points = load_case()
        vertices, edges = min_tree(points)

        resp = sum([distancia_puntos(points[s], points[e]) for s, e in edges])
        print('%.2f'%resp)

        if casos > i+1:
            print('')
main()
