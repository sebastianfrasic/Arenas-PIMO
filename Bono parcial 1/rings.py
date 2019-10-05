from sys import stdin
primos = {1,2,3,5,7,11,13,17,19,23,29,31,37,41,43}
def back(a):
    global num,conjunto
    if len(a) == num:
        if a[-1] + a[0] in primos:
            print(*a)
    else:
        for valor in range(2,num+1):
            if valor not in conjunto and a[-1]+valor in primos:
                if valor not in a:
                    conjunto.add(valor)
                    back(a+[valor])
                    conjunto.remove(valor)
                
def main():
    caso = 0
    
    global num,conjunto
    conjunto = set()
    num = stdin.readline().strip()
    while num:
        num = int(num)
        caso +=1
        if num%2==1:
            print('Case {}:'.format(caso))
            print()
        else:
            print('Case {}:'.format(caso))
            back([1])
            print()
        num = stdin.readline().strip()
main()
