import sys
from collections import deque
input = sys.stdin.readline
cnt = 0
def dfs(start, count):
    visited.add(start)
    for item in family[start]:
        if start == p2:
            print(count)
            exit(0)
        if item not in visited:
            dfs(item, count+1)

    visited.remove(start)


n = int(input())
p1, p2 = map(int, input().split())
r = int(input())
family = [[]*0 for _ in range(n+1)]
visited = set()
for _ in range(r):
    a, b = map(int, input().split())
    family[a].append(b)
    family[b].append(a)
dfs(p1,cnt)
print(-1)