import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
cnt = 0
dx,dy = (-1, 1, 0, 0), (0, 0, -1 ,1)
area = []
val = 0
def dfs(x, y):
    global val
    arr[x][y] = 0
    for i in range(4):
        rx = x+ dx[i]
        ry = y + dy[i]
        if(0<= rx < m) and (0<= ry < n):
            if arr[rx][ry] != 0:
                val +=1
                dfs(rx,ry)

m, n, k = map(int, input().split())
arr = [[1 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split()) #(0,2), (4,4)
    for i in range(y1, y2): #(2,4)
        for j in range(x1, x2): #(0,4)
            arr[i][j] = 0 # 0

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            dfs(i,j)
            area.append(val+1)
            val = 0
            cnt+=1
area.sort()

print(cnt)
for item in area:
    print(item, end =' ')
