from collections import deque
import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())
ok = [[False] * (b+1) for _ in range(a+1)]
answer = []
queue = deque()

def pour(x,y):
    if not ok[x][y]:
        ok[x][y] = True
        queue.append((x,y))

def bfs():
    queue.append((0,0))
    ok[0][0] = True
    while queue:        
        x,y = queue.popleft()
        z = c - x - y #c 물의 양 도출
        
        if x == 0:
            answer.append(z)        

        # x-> y
        water = min(x,b-y)
        pour(x-water, y+water)
        # x-> z
        water = min(x,c-z)
        pour(x-water, y)
        # y-> x
        water = min(y,a-x)
        pour(x+water, y-water)        
        # y-> z
        water = min(y,c-z)
        pour(x,y-water)
        # z-> x
        water = min(z,a-x)
        pour(x+water,y)
        # z-> y
        water = min(z,b-y)
        pour(x,y+water)


bfs()
print(*sorted(answer))