from sys import stdin

def main():
    casos = stdin.readline().strip()
    while casos:
        pila = []
        cola = []
        cp = []
        pila1 = True
        cola1 = True
        cp1 = True
        insert = 0
        delete = 0
        for i in range(int(casos)):
            x = list(map(int,stdin.readline().split()))
            if x[0] == 1:
                insert = insert + 1
                pila.append(x[1])
                cola.append(x[1])
                cp.append(x[1])
            else:
                delete = delete + 1
                
                if (delete <= insert):
                    if pila1 == True:
                        if pila[-1] == x[1]:
                            pila.pop()
                        else:
                            pila1 = False
                    if cola1 == True:
                        if cola[0]==x[1]:
                            cola.pop(0)
                        else:
                            cola1 = False
                    if cp1 == True:
                        maximo = max(cp)
                        if maximo == x[1]:
                            cp.remove(maximo)
                        else:
                            cp1 = False
                else:
                    pila1 = False
                    cola1 = False
                    cp1 = False
        if (pila1 == True) and (cola1 == False) and (cp1 == False):
            print("stack")
        elif (pila1 == False) and (cola1 == True) and (cp1 == False):
            print("queue")
        elif (pila1 == False) and (cola1 == False) and (cp1 == True):
            print("priority queue")
        elif (pila1 == False) and (cola1 == False) and (cp1 == False):
            print("impossible")
        else:
            print("not sure")

                
        casos = stdin.readline().strip()
main()
