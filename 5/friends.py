from sys import stdin

class seet():
    def __init__(self,x):
        self.p = self
        self.rank = 0
        self.key = x
        self.lenght = 1
    

def find_set(x):
    if x != x.p:
        x.p = find_set(x.p)
    return x.p

def link(x,y):
    if x.rank > y.rank:
        y.p = x
        x.lenght += y.lenght
    else:
        x.p = y
        y.lenght += x.lenght
        if x.rank == y.rank:
            y.rank += 1


def union(x,y):
    z = find_set(x)
    u = find_set(y)
    if z != u:
        link(u,z)
    

def main():
    
    casos = int(stdin.readline().strip())
    for i in range(casos):
        red = {}
        n = int(stdin.readline().strip())
        for k in range(n):
            x, y = stdin.readline().strip().split()
            if x == y:
                if x not in red:
                    red[x] = seet(x)
            else:
                if x not in red:
                    red[x] = seet(x)
                if y not in red:
                    red[y] = seet(y)
                union(red[x],red[y])
            print(find_set(red[x]).lenght)
                    

main()
                    
