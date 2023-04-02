import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input()) #노드 개수
cnt = 0
arr = [[] for _ in range(n+1)]
depth = [0 for _ in range(n+1)]
ok = [False for _ in range(n+1)]

def dfs(n):
    ok[n] = True
    for i in arr[n]:
        if not ok[i]: #방문하지 않았다면
            depth[i] = depth[n] + 1
            dfs(i)

for _ in range(n-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
dfs(1)

for i in range(2,n+1): #1,2
    if len(arr[i]) == 1:
        cnt += depth[i]
if cnt % 2 == 0:
    print("No")
else:
    print("Yes")

