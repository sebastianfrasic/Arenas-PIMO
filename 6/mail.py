from sys import stdin
import heapq
def relax(u,v,w):
    global distance,q
    if distance[v]>distance[u]+w:
        distance[v] = distance[u]+w
        heapq.heappush(q,(distance[u]+w,v))
def main():
    global distance,q
    n = int(stdin.readline())
    for i in range(n):
        line =list(map(int,stdin.readline().split()))
        l=[[]for k in range(line[0])]
        for j in range(line[1]):
            conex = list(map(int,stdin.readline().split()))
            l[conex[0]].append((conex[1],conex[2]))
            l[conex[1]].append((conex[0],conex[2]))
        distance = [float("inf")for k in range(line[0])]
        distance[line[2]] = 0
        q = []
        heapq.heappush(q,(0,line[2]))
        while q:
            d, u = heapq.heappop(q)
            if distance[u] !=float("inf"):
                for v,w in l[u]:
                    relax(u,v,w)
        if distance[line[3]] != float("inf"):
            print("Case #{}: {}".format(i+1,distance[line[3]]))
        else:
            print("Case #{}: unreachable".format(i+1)) 
            
main()

            
            
