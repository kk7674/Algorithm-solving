import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0 ,0 ,- 1, 1)

def bfs(a,b):
    q = deque()
    q.append((a,b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            rx = x + dx[i]
            ry = y + dy[i]
            if (0<=rx<n) and (0<=ry<m):
                if arr[rx][ry] == 1:
                    arr[rx][ry] = arr[x][y] + 1
                    q.append((rx,ry))
bfs(0,0)
print(arr[n-1][m-1])



