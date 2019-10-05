from sys import stdin
def main():
    n = int(stdin.readline())
    vacio = stdin.readline()
    for i in range(n):
        print("Case #{}:".format(i+1))
        matriz = []
        entrada = stdin.readline().split()
        while len(entrada) != 0:
            matriz.append(entrada)
            entrada = stdin.readline().split()
        for x in range(len(matriz)):
            j = 0
            k = 0
            palabra = ""
            while j < len(matriz[x]):
                if k < len(matriz[x][j]):
                    palabra += matriz[x][j][k]
                    j+=1
                    k+=1
                else:
                    j+=1
            print(palabra)    
        print()
main()
