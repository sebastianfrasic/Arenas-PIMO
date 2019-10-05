from sys import stdin
def suma (a,t,i):
    if t == 23 and i > len(a)-1:
        return True
    elif i>=len(a):
        return False
    else:    
        return suma(a,t-int(a[i]),i+1) or suma(a,t+int(a[i]),i+1) or suma(a,t*int(a[i]),i+1)
    
def main():
    a = stdin.readline().split()
    res = suma(a,int(a[0]),1)
    if res == True:
        print("Possible")
    else: 
        print("Impossible")
main()
