from sys import stdin

def main():
    datos = list(map(int,stdin.readline().strip().split()))
    while len(datos) > 0:
        n = datos[0]
        m = datos[1]
        t = datos[2]
        memo = [-1 for i in range(t+1)]
        if n == 1 or m == 1:
            print(t)
        else:
            memo[0] = 0
            for i in range(t+1):
                tn = 0
                tm = 0
                if i-n >= 0:
                    tn = memo[i-n]+1
                if i-m >= 0:
                    tm = memo[i-m]+1
                if max(tn,tm) > 0:
                    memo[i] = max(tn,tm)
            if memo[t] >= 0:
                print(memo[t])
            else:
                for i in range(t-1,-1,-1):
                    if memo[i] >= 0:
                        print(memo[i],t-i)
                        break
        datos = list(map(int,stdin.readline().strip().split()))
main()
        
                        
