from sys import stdin
def findpadre(x):
    global padre,rank
    p=padre[x]
    if p!=x:
        padre[x]=findpadre(padre[x])
    return padre[x]
def union(x,y):
    global padre,rank
    xp=findpadre(x)
    yp=findpadre(y)
    if xp!=yp:
        if rank[xp]>rank[yp]:
            padre[yp]=xp
            rank[xp]+=1
        else:
            padre[xp]=yp
            rank[yp]+=1
        return True
    return False
def kruskal(adj):
    total=0
    for arco in adj:
        if union(arco[1],arco[2]):
            total+=arco[0]
    return total
def minimo(st1,st2):
    res = 0
    for i in range(4):
        res +=min(abs(int(st1[i])-int(st2[i])),10-abs(int(st1[i])-int(st2[i])))
    return res
def main():
    global padre,rank
    x = int(stdin.readline().strip())
    for i in range(x):
        dic = {}
        inicial = '0000'
        ady = []
        minimus =  []
        lista = stdin.readline().strip().split()
        casos = int(lista.pop(0))+1
        padre=[i for i in range(casos)]
        rank=[0 for i in range(casos)]
        ini = 0
        for j in lista:
            dic[j] = ini
            ini += 1
            minimus.append(minimo(inicial,j))
        minimus = min(minimus)
        while len(lista) != 1:
            nodo = lista.pop(0)
            for k in lista:
                dista = (minimo(nodo,k),dic[nodo],dic[k])
                ady.append(dista)
        ady.sort()
        ans = kruskal(ady)
        print(ans+minimus)   
main()
