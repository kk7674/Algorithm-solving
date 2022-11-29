import sys
input = sys.stdin.readline
mini = sys.maxsize
tem_sd = -1
N, M, B = map(int,input().split())
arr = []
for i in range(N): #세로    
    arr += list(map(int,input().split()))

maxi = int((sum(arr)+B)/(N*M))
total = 0
for s in range(maxi+1):
    for h in arr:
        if h > s:
            total += 2*(h - s)            
        elif h < s:
            total += (s - h)            
                   
    if mini >= total:
        mini = total
        tem_sd = s
    
    total = 0
print(mini, tem_sd)