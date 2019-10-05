from sys import stdin

class seet():
    def __init__(self,x):
        self.p = self
        self.rank = 0
        self.key = x

    

def find_set(x):
    if x != x.p:
        x.p = find_set(x.p)
    return x.p

def link(x,y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1


def union(x,y):
    z = find_set(x)
    u = find_set(y)
    link(u,z)
    

def main():
    
    casos = int(stdin.readline().strip())
    empty = stdin.readline()
    for i in range(casos):
        good = 0
        wrong = 0
        n = int(stdin.readline().strip())
        nodos = {}
        for k in range(n):
            nodos[k+1] = seet(k+1)
            
        datos = stdin.readline().strip().split()
        while len(datos) == 3:    
            op = datos[0]
            a = int(datos[1])
            b = int(datos[2])
                

            n1 = nodos[a]
            n2 = nodos[b]

            if op == "q":
                if find_set(n1) == find_set(n2):
                    good += 1
                else:
                    wrong += 1
                
            else:
                union(n1,n2)
                
            datos = stdin.readline().strip().split()
        print("{},{}".format(good,wrong))   
        if i < casos-1:
            print()
        



main()
                    

