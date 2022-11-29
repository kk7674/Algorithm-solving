import sys
input = sys.stdin.readline

n, k = list(map(int,input().split()))
temp = []
for i in range(n):
    temp.append(int(input()))
cnt = 0
idx = -1
while k > 0:
    cnt += int(k // temp[idx])
    k %= temp[idx]
    idx -= 1    
print(cnt)