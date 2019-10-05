from sys import stdin


def par(num):
    cont = 0
 
    while num != 1:
        cont += 1
        if num % 2 == 0:
            num = num//2 
        else: 
            num = (3*num)+1
    cont += 1

    return cont



def veces(x,y):
    x, y = min(x, y), max(x,y)
    return max(par(i) for i in range(x, y+1))


def main():

    a = list(map(int, stdin.readline().strip().split()))
    
    while len(a) != 0:
        x = a[0]
        y = a[1]
        print (x , y, veces(x,y))
        a = list(map(int, stdin.readline().strip().split()))


    
main()

