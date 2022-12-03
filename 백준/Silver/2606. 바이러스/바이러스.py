import sys
input = sys.stdin.readline

n = int(input())
pair = int(input())
cnt = 0
visited = [False]*(n+1)
network=[[]* 0 for _ in range(n+1)] #0번 안쓰니까 1 늘려줌

def dfs(graph, v, visited):    
    global cnt
    visited[v] = True        

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            cnt+=1

for i in range(1, pair+1):
    a, b =list(map(int,input().split()))
    network[a].append(b)
    network[b].append(a)

dfs(network,1,visited)
print(cnt)