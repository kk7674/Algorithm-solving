import sys
input = sys.stdin.readline

N, S, M = map(int,input().split())
V = list(map(int,input().split()))

dp = [[0] * (M+1) for _ in range(N+1)]
dp[0][S] = 1 #스타트 포인트

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 1:
            num1 = j - V[i]
            num2 = j + V[i]
            if 0 <= num1 and num1 <= M:
                dp[i+1][num1] = 1
            if 0 <= num2 and num2 <= M:
                dp[i+1][num2] = 1

ans = -1
for i in range(M+1):
    if dp[N][i] == 1:
        ans = i
            
print(ans)


