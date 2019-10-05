from sys import stdin

def homero(lista, m, n, t):
        if m != 1 or n != 1:
            lista[0] = 0
            for j in range(t+1):
                tn = 0
                tm = 0
                if j-m >= 0:
                    tn = 1+lista[j-m]
                if j-n >= 0:
                    tm = 1+lista[j-n]
                if max(tm,tn) > 0:
                    lista[j] = max(tm,tn)
            if lista[t] < 0:
                for j in range(-1+t,-1,-1):
                    if lista[j] >= 0:
                        return [lista[j],t-j]
                        break
            else:
                return [lista[t]]
            
        else:
            return [t]


def main():
    entrada = list(map(int,stdin.readline().strip().split()))
    while True:
        if len(entrada) <= 0:
            break
        else:
    
            m = entrada[0]
            n = entrada[1]
            t = entrada[2]
            lista = [-1 for i in range(1+t)]

            resp = homero(lista, m, n, t)

            print(*resp)
            
            entrada = list(map(int,stdin.readline().strip().split()))
main()
