import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
dx = [1, -1, 0 ,0, -1, -1, 1, 1]
dy = [0 ,0 , 1, -1, -1, + 1, -1, 1]
cnt = 0

def dfs(x,y):
    global cnt    
    mapp[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<=nx<m) and (0<=ny<n):
            if(mapp[nx][ny] == 1):
                dfs(nx,ny)

n=1
m=1
mapp = []
while True:
    n, m = map(int, input().split()) #너비 높이
    if n == 0 and m == 0:
        exit(0)
    for _ in range(m):
        mapp.append(list(map(int, input().split())))    
    for i in range(m):
        for j in range(n):            
            if mapp[i][j] == 1:                
                dfs(i, j)
                cnt+=1
    print(cnt)                 
    cnt = 0
    mapp.clear()
