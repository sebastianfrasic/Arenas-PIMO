from sys import stdin
import heapq

def main():
    global distance,q
    x = int(stdin.readline())
    for i in range(x):
        n = int(stdin.readline())
        m = int(stdin.readline())
        matriz = []
        for j in range(n):
            line = [int(k) for k in stdin.readline().split()]
            matriz.append(line)
        distance = [[float("inf")for k in range(m)]for y in range(n)]
        visit = [[0 for k in range(m)]for y in range(n)]
        distance[0][0] = matriz[0][0]
        q = []
        heapq.heappush(q,(matriz[0][0],[0,0]))
        x = [-1,0,0,1]
        y = [0,-1,1,0]
        while q:
            d,u = heapq.heappop(q)
            if not visit[u[0]][u[1]]:
                visit[u[0]][u[1]] = 1
                for k in range(4):
                    v = [u[0]+y[k],u[1]+x[k]]
                    if -1<v[0]<n and -1<v[1]<m:
                        w = matriz[v[0]][v[1]]
                        if distance[v[0]][v[1]]>distance[u[0]][u[1]]+w:
                            distance[v[0]][v[1]] = distance[u[0]][u[1]]+w
                            heapq.heappush(q,(distance[u[0]][u[1]]+w,v))
        print(distance[-1][-1])
main()
        
