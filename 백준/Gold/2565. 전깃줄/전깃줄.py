import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])    

arr.sort()
dp = [1]*n
for i in range(1,n):
    for j in range(0,i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i],dp[j]+1)
print(n - max(dp))