from sys import stdin

def back(res, t, i, lista, empty):
    global contador
    if t == 0:
        if res not in empty:
            contador = contador + 1
            empty.append(res)
    elif t < 0 or len(lista) <= i:
        return None
    else:
        aux = res[:]
        newRes = res[:]
        newRes.append(lista[i])

        return back(aux,t,i+1,lista,empty) or back(newRes,t-lista[i],i+1,lista,empty)

def main():
    global contador
    entrada = list(map(int,stdin.readline().strip().split()))
    while (entrada[0] != 0 or entrada[1] != 0):
        lista = entrada[2:]
        t = entrada[0]
        print("Sums of {}:".format(t))
        empty = []
        res = []
        contador = 0
        back(res,t,0,lista,empty)
        if contador == 0:
            print("NONE")
        else:
            print(contador)
        entrada = list(map(int,stdin.readline().strip().split()))

main()
