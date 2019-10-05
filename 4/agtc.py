from sys import stdin

def cadena(n,m):
    global c1, c2
    mat = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(1,n+1):
        mat[0][i] = i
    for j in range(1,m+1):
        mat[j][0] = j

    for j in range(1,m+1):
        for i in range(1,n+1):
            if c1[i-1] == c2[j-1]:
                mat[j][i] = mat[j-1][i-1]
            else:
                mat[j][i] = min(1 + mat[j-1][i-1],1 + mat[j][i-1],1 + mat[j-1][i])
                
            
    return mat[m][n]



def main():
    global c1,c2
    x = stdin.readline().strip().split()
    while x:
        c1 = x[1]
        
        c2 = stdin.readline().strip().split()
        c2 = c2[1]
        n = len(c1)
        m = len(c2)
        resp = cadena(n,m)
        print(resp)
        x = stdin.readline().strip().split()
main()
