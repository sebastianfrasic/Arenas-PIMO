from sys import stdin
from collections import deque
def bfs(s):
    global m,a,b
    visit =[[0 for i in range(b)]for j in range(a)]
    distance = [[0 for i in range(b)]for j in range(a)]
    visit[s[0]][s[1]] = 1
    distance[s[0]][s[1]] = 0
    q = deque()
    q.append(s)
    x = [-1,0,0,1]
    y = [0,-1,1,0]
    while len(q) != 0:
        u = q.popleft()
        for i in range(4):
            v = [u[0]+y[i],u[1]+x[i]]
            if -1<v[0]<a and -1<v[1]<b and m[v[0]][v[1]]:
                if not visit[v[0]][v[1]]:
                    visit[v[0]][v[1]] = 1
                    distance[v[0]][v[1]] = distance[u[0]][u[1]]+1
                    q.append(v)
    return distance
            


def main():
    global m,a,b
    a ,b = list(map(int,stdin.readline().split()))
    while a + b != 0:
        m  = [[1 for i in range(b)] for j in range(a)]
        bom = int(stdin.readline())
        for i in range(bom):
            line = list(map(int,stdin.readline().split()))
            for j in range(line[1]):
                m[line[0]][line[2+j]] = 0
        ini = list(map(int,stdin.readline().split()))
        fin = list(map(int,stdin.readline().split()))
        print(bfs(ini)[fin[0]][fin[1]])
        a ,b = list(map(int,stdin.readline().split()))
main()
