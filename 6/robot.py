from sys import stdin

def dfs(casilla, visit, time, data):
    visit[casilla[0]][casilla[1]] = 1
    if data [casilla[0]][casilla[1]] == "N":
        casilla[0] = casilla[0] - 1
    elif data [casilla[0]][casilla[1]] == "W":
        casilla[1] = casilla[1] - 1
    elif data [casilla[0]][casilla[1]] == "E":
        casilla[1] = casilla[1]+ 1
    else:
        casilla[0] = casilla[0] + 1
    return dfs_visit(casilla,1, visit, time, data)


def dfs_visit(casilla, tiempo, visit, time, data):
    if (casilla[0] < 0) or (len(data) <= casilla[0]) or (casilla[1] < 0) or (len(data[0]) <= casilla[1]):
        print(str(tiempo) + " step(s) to exit")
    else:
        if visit[casilla[0]][casilla[1]] == False:
            time[casilla[0]][casilla[1]] = time[casilla[0]][casilla[1]] + tiempo
            visit[casilla[0]][casilla[1]] = 1
                    
            if data [casilla[0]][casilla[1]] == "N":
                casilla[0] = casilla[0] - 1
            elif data [casilla[0]][casilla[1]] == "W":
                casilla[1] = casilla[1] - 1
            elif data [casilla[0]][casilla[1]] == "E":
                casilla[1] = casilla[1]+ 1
            else:
                casilla[0] = casilla[0] + 1
            dfs_visit(casilla, tiempo+1, visit, time, data)
        else:
            resp = time[casilla[0]][casilla[1]]
            print(str(resp) + " step(s) before a loop of " + str(tiempo-resp) + " step(s)")

def main():
    x,y,z = [int(n) for n in stdin.readline().split()]
    while x != 0 and y != 0 and z != 0:
        data = []
        for i in range(x):
            data.append(stdin.readline().strip())
        visit = [[0 for i in range(y)] for j in range(x)]
        time = [[0 for i in range(y)] for j in range(x)]
        dfs([0, z-1], visit, time, data)
        x,y,z = [int(n) for n in stdin.readline().split()]

main()
