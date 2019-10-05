from sys import stdin

def suma(num):
    if num <= 9 :
        return num
    else:
        return suma(sum(list(map(int, str(num)))))


def main():
    x = stdin.readline().strip().split()
    n = x[0]
    veces = int(x[1])
    num = n * veces


    print(suma(int(num)))

main()
