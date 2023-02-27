#모든 위치에서 시작할 수 있게 반복문 세팅
#set으로 겹치는 것들 없애
#문자열로 ㄱㄱ
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx,dy = (-1,1,0,0),(0,0,-1,1)
temp = []
s1 = set([])
cnt = 0
def dfs(x,y, number):
    number += arr[x][y]
    if len(number) == 6:
        s1.add(number)
        return
    else:
        for i in range(4):
            rx = x + dx[i]
            ry = y + dy[i]
            if (0<=rx<5) and (0<=ry<5):
                dfs(rx,ry,number)


arr = [list(map(str,input().split())) for _ in range(5)]
for i in range(5): #줄
    for j in range(5):
        dfs(i,j,"")
print(len(s1))
