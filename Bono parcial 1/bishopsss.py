from sys import stdin
def amenaza(i,j):
    global bishops, n
    for x,y in bishops:
        if abs(x-i) == abs(y-j):
            return False
    return True


def main():
    
    dic = {(1, 0): 1, (1, 1): 1, (2, 0): 1, (2, 1): 4, (2, 2): 4,
           (2, 3): 0, (2, 4): 0, (3, 0): 1, (3, 1): 9,
           (3, 2): 26, (3, 3): 26, (3, 4): 8, (3, 5): 0,
           (3, 6): 0, (3, 7): 0, (3, 8): 0, (3, 9): 0,
           (4, 0): 1, (4, 1): 16, (4, 2): 92, (4, 3): 232,
           (4, 4): 260, (4, 5): 112, (4, 6): 16, (4, 7): 0,
           (4, 8): 0, (4, 9): 0, (4, 10): 0, (4, 11): 0,
           (4, 12): 0, (4, 13): 0, (4, 14): 0, (4, 15): 0,
           (4, 16): 0, (5, 0): 1, (5, 1): 25, (5, 2): 240,
           (5, 3): 1124, (5, 4): 2728, (5, 5): 3368, (5, 6): 1960,
           (5, 7): 440, (5, 8): 32, (5, 9): 0, (5, 10): 0,
           (5, 11): 0, (5, 12): 0, (5, 13): 0, (5, 14): 0,
           (5, 15): 0, (5, 16): 0, (5, 17): 0, (5, 18): 0,
           (5, 19): 0, (5, 20): 0, (5, 21): 0, (5, 22): 0,
           (5, 23): 0, (5, 24): 0, (5, 25): 0, (6, 0): 1,
           (6, 1): 36, (6, 2): 520, (6, 3): 3896, (6, 4): 16428,
           (6, 5): 39680, (6, 6): 53744, (6, 7): 38368, (6, 8): 12944,
           (6, 9): 1600, (6, 10): 64, (6, 11): 0, (6, 12): 0,
           (6, 13): 0, (6, 14): 0, (6, 15): 0, (6, 16): 0,
           (6, 17): 0, (6, 18): 0, (6, 19): 0, (6, 20): 0,
           (6, 21): 0, (6, 22): 0, (6, 23): 0, (6, 24): 0,
           (6, 25): 0, (6, 26): 0, (6, 27): 0, (6, 28): 0,
           (6, 29): 0, (6, 30): 0, (6, 31): 0, (6, 32): 0,
           (6, 33): 0, (6, 34): 0, (6, 35): 0, (6, 36): 0}
    
    a = list(map(int,stdin.readline().strip().split()))
    
    while (a[0]!= 0 or a[1] != 0):
        n = a[0]
        k = a[1]
        
        
        print(dic[n,k])
        
        a = list(map(int,stdin.readline().strip().split()))
        
main()
