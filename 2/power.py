from sys import stdin
def back(x,n,i):
    if x == 0:
        return 1
    elif x < 0 or (i**n) > x:
        return 0
    else:
        return back(x-(i**n),n,i+1) + back(x,n,i+1)
        
def main():
    x = stdin.readline().strip()
    while x:
        n = stdin.readline().strip()
        x = int(x)
        n = int(n)
        print(back(x,n,1))
        x = stdin.readline().strip()
        
main()
