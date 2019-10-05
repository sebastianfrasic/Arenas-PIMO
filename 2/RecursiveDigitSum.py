from sys import stdin

def sumarec(a):
    if len(a) == 1:
        return a[0]
    else:
        return a[0] + sumarec(a[1:])


def numCif(n):
    if int(n) < 10:
        return 1
    else:
        return 1 + numCif(int(n)//10)



def suma(num):
    lista = []
    for i in range(len(num)):
        lista.append(num[i])
    lista = list(map(int,lista))

    return sumarec(lista)

def recurrencia(num):
    if numCif(num) == 1:
        return num
    else:
        return recurrencia(str(suma(num)))
        
        

def main():

    x = stdin.readline().strip().split()
    n = x[0]
    veces = int(x[1])
    
    num = n * veces

    cif = numCif(num)
    
    

    print(recurrencia(str(suma(num))))


main()

    


