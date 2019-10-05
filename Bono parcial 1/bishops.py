from sys import stdin

def amenaza(i,j):
    global bishops, n
    for x,y in bishops:
        if abs(x-i) == abs(y-j):
            return False
    return True

def back(i,j):
    global n,k,cont,bishops
    if len(bishops) == k:
        cont = cont + 1
        return None
    if i == n:
        return None

    newI, newJ = i, j+1
    if newJ >= n:
        newI += 1
        newJ = 0
    if amenaza(i,j):
        bishops.append((i,j))
        back(newI, newJ)
        bishops.pop()
    back(newI, newJ)


def main():
    global n,k,cont,bishops
    dic = {}
    
    a = list(map(int,stdin.readline().strip().split()))
    for n in range(1,7):
        for k in range(0, (n**2)+1):
            bishops = []
            cont = 0
            back(0,0)
            dic[(n,k)] = cont
    while (a[0]!= 0 or a[1] != 0):
        n = a[0]
        k = a[1]
        
        
        print(dic[n,k])
        
        a = list(map(int,stdin.readline().strip().split()))
        
main()
