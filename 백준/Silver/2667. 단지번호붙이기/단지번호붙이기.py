import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
house = []
result = []
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y): #세로, 가로
    global cnt
    cnt+=1
    house[x][y] = 0
    for i in range(4):
        rx = x + dx[i]
        ry = y + dy[i]
        if (0<= rx <n) and (0<= ry <n):
            if house[rx][ry] == 1:
                dfs(rx, ry)

for _ in range(n):
    house.append(list(map(int, input().rstrip())))

for i in range(n): #세로
    for j in range(n): #가로
        if house[i][j] == 1:
            cnt = 0
            dfs(i,j)
            result.append(cnt)

result.sort()
print(len(result))
for item in result:
    print(item)


