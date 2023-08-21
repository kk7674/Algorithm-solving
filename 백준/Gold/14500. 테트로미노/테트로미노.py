import sys
input = sys.stdin.readline
m, n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]
dx, dy = (-1,1,0,0), (0,0,-1,1)
ok = [[False] * n for _ in range(m)]
maxi = 0

def dfs(a,b,val,step):        
    if step == 4:
        global maxi
        maxi = max(maxi,val)
        return
        
    for i in range(4):
        rx = a + dx[i]
        ry = b + dy[i]
        if 0<=rx<m and 0<=ry<n:
            if ok[rx][ry] == False:
                ok[rx][ry] = True #방문처리
                dfs(rx,ry,val+arr[rx][ry],step+1)
                ok[rx][ry] = False #원상 복구
def exec(a,b):
    global maxi
    for i in range(4): #4가지 조합(ㅗ 모양)
        tmp = arr[a][b]
        for j in range(3): #뽑아야 하는 것 3가지
            t = (i+j)%4
            rx = a + dx[t]
            ry = b + dy[t]
            if not (0<=rx<m and 0<=ry<n):
                tmp = 0                
                break
            tmp+=arr[rx][ry]        
        maxi = max(maxi,tmp)

for i in range(m):
    for j in range(n):
        ok[i][j] = True #방문처리
        dfs(i,j,arr[i][j],1)    
        ok[i][j] = False  
        exec(i,j)  
print(maxi)