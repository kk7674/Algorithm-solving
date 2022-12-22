import sys
input = sys.stdin.readline
import copy
from collections import deque

n, m =map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
queue = deque()
res = 0
def bfs():
    temp_map = copy.deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 2:
                queue.append((i, j))

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            rx = a + dx[i]
            ry = b + dy[i]
            if 0<=rx<n and 0<=ry<m:
                if temp_map[rx][ry] == 0:
                    temp_map[rx][ry] = 2
                    queue.append((rx,ry))
    global res
    count = 0
    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 0:
                count+=1
    res = max(res, count)

def makewall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                makewall(cnt+1)
                arr[i][j] = 0


makewall(0)
print(res)

