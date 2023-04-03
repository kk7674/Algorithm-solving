import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split()) #노드 수, 라인 수
arr = [[] for _ in range(n+1)]
depth = [0 for _ in range(n+1)]
ok = [False] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(n):
    ok[n] = True
    q = deque([])
    q.append(n)
    while q:
        v = q.popleft()
        for i in arr[v]:
            if not ok[i]:
                depth[i] = depth[v] + 1
                q.append(i)
                ok[i] = True

bfs(1)
temp = []
maxi = max(depth)
for idx,item in enumerate(depth):
    if item == maxi:
        temp.append(idx)

print(min(temp), maxi, len(temp))