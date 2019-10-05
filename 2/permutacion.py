from sys import stdin

def permutacion(cadena, i):
    global x
    if len(x) <= i:
        print (cadena)
    else:
        for letra in range(len(cadena)+1):
            s = cadena[:letra] + x[i] + cadena[letra:]
            permutacion(s, i+1)

def main():
    global x
    
    x = stdin.readline().strip()
    while x:
        permutacion(x[0], 1)
        print()
        x = stdin.readline().strip()
main()
        
