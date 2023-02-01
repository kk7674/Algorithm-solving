n = int(input()) # n=7

schedule = []

for _ in range(n):
    schedule.append(list(map(int, input().split())))

dp = [0] * (n+1)

for i in range(n-1, -1, -1): # 6,-1,-1
    if i + schedule[i][0] > n: # 6 + schedule[6][0] > 7, 상담일수 넘어가는 경우
        dp[i] = dp[i+1] # dp[6] = dp[7] = 0
    else: #상담일수 여유 있는 경우
        dp[i] = max(schedule[i][1] + dp[i+schedule[i][0]], dp[i+1])
        #dp[4] = max(schedule[4][1] + dp[4+schedule[4][0]], dp[5])

# print(dp)
print(dp[0])