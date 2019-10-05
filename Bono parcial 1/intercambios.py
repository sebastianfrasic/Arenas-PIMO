from sys import stdin

def unir(low,high,lista):
    contador_final = 0
    if high > low+1:
        mid = low + ((high-low)//2)
        contador_final = unir(low,mid,lista) + unir(mid,high,lista) + Merge_Sort(low,high,mid,lista)
    return contador_final

def Merge_Sort(low,high,mid,lista):
    contador = 0
    i = 0
    j = 0
    first = lista[low:mid]
    second = lista[mid:high] 
    for x in range(low,high):
        if -mid + high == j:
            lista[x] = first[i]
            i = i + 1
        elif (mid-low) == i:
            lista[x] = second[j]
            j = j + 1
        
        else:
            if first[i] > second[j]:
                lista[x] = second[j]
                j = j + 1
                contador = (-i+(mid-low)) + contador
            else:
                lista[x] = first[i]
                i+=1
                
    return contador


def main():
  n = int(stdin.readline().strip())
  while n!=0:
    lista = []
    for i in range(n):
        lista.append(int(stdin.readline().strip()))
    
    resp = unir(0,n,lista)
    
    print(resp)
    n = int(stdin.readline().strip())
main()
