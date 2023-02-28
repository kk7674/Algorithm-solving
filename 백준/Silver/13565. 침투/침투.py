import sys
sys.setrecursionlimit(1000000)
#input = sys.stdin.readline
m,n = map(int,input().split()) # 5,6
arr = [list(map(int,list(input()))) for _ in range(m)]
temp_arr = arr.copy()
dx,dy = (-1,1,0,0),(0,0,-1,1)
def dfs(x,y):
    arr[x][y] = 1
    if x == m-1:
        print("YES")
        exit(0)

    for i in range(4):
        rx = x + dx[i]
        ry = y + dy[i]
        if (0<=rx<m) and (0<=ry<n):
            if arr[rx][ry] == 0:
                dfs(rx,ry)

for idx,item in enumerate(arr[0]):
    if item == 0:
        dfs(0,idx)
        arr = temp_arr.copy()
print("NO")
exit(0)