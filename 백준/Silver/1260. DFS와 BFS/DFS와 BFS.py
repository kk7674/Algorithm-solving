import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M, V = map(int, input().split())
d_visited = [False] * (N+1)
b_visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]


def dfs(start):
    print(start, end=' ')
    d_visited[start] = True
    for i in graph[start]:
        if not d_visited[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    b_visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not b_visited[i]:
                b_visited[i] = True
                queue.append(i)


for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
dfs(V)
print(end = '\n')
bfs(V)





