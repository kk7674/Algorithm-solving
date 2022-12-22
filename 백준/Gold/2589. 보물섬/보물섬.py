import sys
import copy
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
mapp = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
res = 0
final = 0
def bfs(i,j):
    global res
    temp_visited = copy.deepcopy(visited)
    temp_visited[i][j] = 1
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            rx = a + dx[i]
            ry = b + dy[i]
            if 0<=rx<n and 0<=ry<m:
                if mapp[rx][ry] == 'L' and temp_visited[rx][ry] == 0:
                    queue.append((rx,ry))
                    temp_visited[rx][ry] = temp_visited[a][b] + 1
                    res = max(res, temp_visited[rx][ry])


queue = deque()
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 'L':
            queue.append((i,j))
            bfs(i,j)
            final = max(res, final)
print(final-1)
