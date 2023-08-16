import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int,input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1,n+1): #n=3 1,2,3
    for j in range(1,i+1):# 1 -> 1, 2 -> 1,2
        dp[i] = max(dp[i],dp[i-j] + arr[j])
print(dp[n])
