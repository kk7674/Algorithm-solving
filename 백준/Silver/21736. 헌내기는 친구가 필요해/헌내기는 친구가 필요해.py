import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n, m = map(int,input().split())
campus = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx, dy = (-1,1,0,0),(0,0,-1,1)
answer = 0
def dfs(x,y):
    visited[x][y] = 1
    global answer
    if campus[x][y] =="P":
        answer+=1        
    for i in range(4):
        rx = x + dx[i]
        ry = y + dy[i]
        if(0<=rx<n) and (0<=ry<m):
            if campus[rx][ry] != 'X' and visited[rx][ry] == 0:                
                dfs(rx,ry)


for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            dfs(i,j)
            if answer == 0:
                print("TT")
            else:
                print(answer)
            exit(0)