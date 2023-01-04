import sys
input = sys.stdin.readline
n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1,n): #idx 1~4까지 0은 무시
    for j in range(i+1):
        if j==0:
            dp[i][0] += dp[i-1][0]
        elif i==j:
            dp[i][-1] += dp[i-1][-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[-1]))