import sys
input = sys.stdin.readline
n = int(input())
num =[]
dp = [0] * n
for _ in range(n):
    num.append(int(input().rstrip()))
if n <= 2:
    print(sum(num))
    exit(0)
else:    
    dp[0] = num[0]
    dp[1] = num[0] + num[1]
    dp[2] = max(num[1] + num[2], num[0] + num[2], dp[1])    

    for i in range(3, n):
            dp[i] = max(dp[i-2] + num[i], dp[i-3] + num[i-1] + num[i], dp[i-1])
print(dp[-1])
