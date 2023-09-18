import sys
input = sys.stdin.readline
m,n = map(int, input().split())
arr = []
dp = [[0 for _ in range(m)] for _ in range(m)]
sum = 0
for _ in range(m):
    arr.append(list(map(int,input().split())))
    #0~3, 0~3
for i in range(m): #0~3
    for j in range(m): #0~3
        if i == 0 and j == 0:
            dp[i][j] = arr[i][j]
        elif i == 0 and j != 0:
            dp[i][j] = dp[i][j-1] + arr[i][j]
        elif i != 0 and j == 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        else:
            dp[i][j] = dp[i-1][j] + arr[i][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    x1 -=1
    y1 -=1
    x2 -=1
    y2 -=1
    if x1 >= 1 and y1 >= 1:
        print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])
    elif x1 >= 1 and y1 == 0:
        print(dp[x2][y2] - dp[x1-1][y2])
    elif y1 >= 1 and x1 == 0:
        print(dp[x2][y2] - dp[x2][y1-1])
    else:
        print(dp[x2][y2])

