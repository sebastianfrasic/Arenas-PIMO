import sys
from sys import stdin

def suma(num):
    if num <= 9 :
        return num
    else:
        return suma(sum([int(i) for i in str(num)]))

def mult(x,n):
    return suma(suma(x)*n)

def main():
    for i in sys.stdin:
        x, n = map(int,i.strip().split())
        print(mult(x,n))
main()
