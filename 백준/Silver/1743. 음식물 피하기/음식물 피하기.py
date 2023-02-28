import sys
input= sys.stdin.readline
sys.setrecursionlimit(1000000)
storage = []
cnt = 0
dx,dy = (-1,1,0,0),(0,0,-1,1)
def dfs(x,y):
    global cnt
    cnt += 1
    arr[x][y] = 0
    for i in range(4):
        rx = x + dx[i]
        ry = y + dy[i]
        if (0<=rx<m) and (0<=ry<n):
            if arr[rx][ry] == 1: #스레기일 경우
                dfs(rx,ry)

m,n,k = map(int,input().split())
arr = [[0 for _ in range(n)] for _ in range(m)]

for i in range(k):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1 #쓰레기

for i in range(m): #3 -> 0~2
    for j in range(n): #4 -> 0~3
        if arr[i][j] == 1:
            dfs(i,j)
            storage.append(cnt)
            cnt = 0
print(max(storage))


