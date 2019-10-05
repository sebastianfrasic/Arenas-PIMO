from sys import stdin
import sys
sys.setrecursionlimit(10000000)


def coin(valor,moneda):
    global dp
    for i in range(len(dp)):
        dp[i][0] = 1
    for i in range(len(moneda)):
        for j in range(1,len(dp[0])):
            if moneda[i] <= j:
                dp[i][j] = dp[i-1][j] + dp[i][j-moneda[i]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp
def main():
    global dp
    n = stdin.readline().strip().split(" ")
    valor,moneda = 300,[i for i in range(301)]
    dp = [[0 for i in range(valor+1)] for i in range(len(moneda)+1)]
    coin(valor,moneda)
    while n:
        if n[0]=="":
            break
        elif len(n) == 1:
            print(dp[int(n[0])][int(n[0])])
        elif len(n) == 2:
            valor = int(n[0])
            if valor < int(n[1]):                
                print(dp[int(n[0])][int(n[0])])
            else: 
                print(dp[int(n[1])][int(n[0])])
        elif len(n) == 3:
            valor = int(n[0])
            if valor < int(n[1]):
                a = dp[int(n[0])][int(n[0])]
            else:
                if int(n[1]) == 0:
                    a = 0
                else:
                    a = dp[int(n[1])-1][int(n[0])]
            if valor < int(n[2]):                
                b = dp[int(n[0])][int(n[0])]
            else: 
                b = dp[int(n[2])][int(n[0])]
            
            print(b-a)
        n = stdin.readline().strip().split(" ")
main()
