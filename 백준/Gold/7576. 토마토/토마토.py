import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
queue = deque([])
tomato = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j)) #맨처음 익은 토마토들 queue에 다 넣어버리기

def bfs(): #동서남북 한번씩만 1로 만들고 끝내고 메인에서는
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            rx = x + dx[i]
            ry = y + dy[i]

            if 0<= rx < n and 0<= ry < m:
                if tomato[rx][ry] == 0:
                    tomato[rx][ry] = tomato[x][y] + 1
                    queue.append((rx,ry))

bfs()
maxi = 0
for i in tomato:
    for item in i:
        if item == 0:
            print(-1)
            exit(0)
        maxi = max(maxi, item)
print(maxi-1)