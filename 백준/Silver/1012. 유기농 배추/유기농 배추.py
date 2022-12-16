import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0<=nx<N) and (0<=ny<M): #범위 내에 있고
            if beti[nx][ny] == 1: #배추가 있으면
                beti[nx][ny] = -1
                dfs(nx,ny)

T = int(input())
for i in range(T):
    M, N, K = map(int, input().split()) 
    beti = [[0]*M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        m,n = map(int, input().split())
        beti[n][m] = 1
    
    for i in range(N): #바깥
        for j in range(M): #안
            if beti[i][j] > 0: # 배추가 있을 경우
                dfs(i,j)
                cnt+=1
    print(cnt)