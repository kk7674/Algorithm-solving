import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0,-1, 1]
cnt1 = 0
cnt2 = 0
section = []

def dfs_normal(x,y,c):
    section[x][y] = 0
    for i in range(4):
        rx = x+ dx[i]
        ry = y + dy[i]
        if (0<= rx < N) and (0<= ry < N):
            if section[rx][ry] == c: #해당 컬러
                dfs_normal(rx,ry,c)

def dfs_disabled(x, y, c):
    cpy_section[x][y] = 0
    for i in range(4):
        rx = x + dx[i]
        ry = y + dy[i]
        if (0 <= rx < N) and (0 <= ry < N):
            if cpy_section[rx][ry] == c:  # 해당 컬러
                dfs_disabled(rx, ry, c)

N = int(input())
for _ in range(N):
    section.append(list(map(str, input().rstrip())))

cpy_section = copy.deepcopy(section)

for i in range(N):
    for j in range(N):
        if section[i][j] != 0:
            dfs_normal(i,j,section[i][j])
            cnt1+=1
        if cpy_section[i][j] == 'R':
            cpy_section[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if cpy_section[i][j] != 0:
            dfs_disabled(i, j, cpy_section[i][j])
            cnt2 += 1

print(cnt1, end= ' ')
print(cnt2)
