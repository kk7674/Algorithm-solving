import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
m,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]
cnt = 0

dx,dy = (-1, 1, 0, 0, -1 ,- 1, 1, 1),(0, 0, -1 ,1 ,-1 ,1 , -1 ,1)
def dfs(x,y):
    arr[x][y] = 0
    for i in range(8):
        rx = x + dx[i]
        ry = y + dy[i]
        if (0<=rx<m) and (0<=ry<n):
            if arr[rx][ry] == 1:
                dfs(rx,ry)

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            dfs(i,j)
            cnt+=1
print(cnt)
