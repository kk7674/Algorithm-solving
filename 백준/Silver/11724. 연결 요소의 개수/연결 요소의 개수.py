import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n,m = map(int, input().split())
cnt = 0
visited = [False] * (n+1) #0번 안 쓸거임
graph = [[]*0 for _ in range(n+1)] # 0~6번 만들어야함 d는 5

def dfs(node: int):
    visited[node] = True

    for item in graph[node]:
        if not visited[item]:
            dfs(item)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1): # 1~ 3
    if visited[i] == False:
        if len(graph[i]) != 0:
            dfs(graph[i][0])
            cnt+=1
        else:
            cnt+=1
print(cnt)