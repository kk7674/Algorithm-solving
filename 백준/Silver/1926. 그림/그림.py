import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n,m = map(int,input().split())
graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(n):
    graph.append(list(map(int,input().split())))

def dfs(x,y):
    global cnt
    cnt += 1
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<n and -1<ny<m and graph[nx][ny]==1:
            dfs(nx,ny)

num_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt=0
            dfs(i,j)
            num_list.append(cnt)

if len(num_list)==0:
    print(len(num_list))
    print(0)
else:
    print(len(num_list))
    print(max(num_list))