from sys import stdin
import sys
sys.setrecursionlimit(10000000)

def solve(n,v, dic):
    global coins
    if (n,v) in dic:
        return dic[(n,v)]
    ans = 0
    
    if v == 0:
        ans = 1
    elif v != 0 and n == 0:
        ans = 0
    elif v > 0 and coins[n] > v:
        ans = solve(n-1, v,  dic)
    elif v > 0 and coins[n] <= v:
        ans = solve(n, v-coins[n],  dic) + solve(n-1, v,  dic)

    dic[(n,v)] = ans
    return ans

def main():
    global coins
    n = list(map(int,stdin.readline().split()))
    dic = {}
    while n:
        if len(n) == 1:
            coins = [x for x in range(n[0]+1)]
            resp = solve(n[0],n[0],dic)
            print(resp)
        elif len(n) == 2:
            if n[1]>n[0]:
                coins = [x for x in range(n[0]+1)]
                resp = solve(n[0],n[0],dic)
                print(resp)
            else:
                coins = [x for x in range(n[1]+1)]
                resp = solve(n[1],n[0],dic)
                print(resp)
        else:
            if n[2]> n[0]:
                coins = [x for x in range(n[0]+1)]
                a = solve(n[0],n[0],dic)
            else:
                coins = [x for x in range(n[2]+1)]
                a = solve(n[2],n[0],dic)
            if n[1]> n[0]:
                coins = [x for x in range(n[0]+1)]
                b = solve(n[0],n[0],dic)
            else:
                if n[1]==0:
                    b =0
                else:
                    coins = [x for x in range(n[1]+1)]
                    b = solve(n[1]-1,n[0],dic)
            print(a-b)
        n = list(map(int,stdin.readline().split()))
main()
