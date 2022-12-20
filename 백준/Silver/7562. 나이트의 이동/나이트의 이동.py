import sys
from collections import deque
input = sys.stdin.readline

dx, dy = (-2, -1, 2, 1, -2, -1, 2, 1), (1, 2, 1, 2, -1, -2, -1, -2)
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        a, b = queue.popleft()

        for i in range(8):
            rx = a + dx[i]
            ry = b + dy[i]
            if (0<= rx < l) and (0<= ry <l):
                if arr[rx][ry] == 0:
                    arr[rx][ry] = arr[a][b] + 1
                    queue.append((rx,ry))
    return arr[x2][y2]

n = int(input())
for _ in range(n):
    l = int(input())
    arr = [[0 for _ in range(l)] for _ in range(l)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(0)
    else:
        print(bfs(x1, y1))
