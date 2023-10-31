import sys
input = sys.stdin.readline
T = int(input())
cnt = 0
for _ in range(T):
    P = int(input()) 
    arr = [list(map(int,input().split())) for _ in range(P)]
    arr.sort()
    top = arr[0][1]
    for i in range(1,P):#1~4
        if arr[i][1] < top:
            top = arr[i][1]
        else:
            cnt+=1
    print(P-cnt)
    cnt = 0



