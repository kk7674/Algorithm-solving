import sys
sys.setrecursionlimit(1000000)

n = int(input())
arr = []
ok = [[False for _ in range(n)] for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int,input().split())))

def dfs(x,y):
    if x==n-1 and y==n-1:
        print("HaruHaru")
        exit(0)
    ok[x][y] = True
    dx, dy = (0, arr[x][y]), (arr[x][y], 0)
    for i in range(2):
        rx = x + dx[i]
        ry = y + dy[i]
        if (0<=rx<n) and (0<=ry<n):
            if not ok[rx][ry]:
                dfs(rx,ry)


dfs(0,0)
print("Hing")