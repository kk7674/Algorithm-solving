import sys
input = sys.stdin.readline

arr = [list(input().rstrip()) for _ in range(5)]
num = 0
maxi = 0
temp = 0
for i in arr:
    temp = len(i)
    if maxi < temp:
        maxi = temp

for _ in range(maxi):#행의 max 길이.
    for i in arr:
        if len(i) >= num+1:
            print(i[num], end='')
    num+=1