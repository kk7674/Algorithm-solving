""

"""
1. 아이디어
점화식: A(N-1) * 2 -1 = A(N)

2. 시간복잡도

3. 자료구조
dp
"""
import sys
n = int(input())
dp = [[0]*10 for _ in range(n)]
#가로 마지막 뭐들어갔는지
#세로 n값
for i in range(1,10): #1~9
    dp[0][i] = 1
if n>=2:
    for a in range(1,n):#n=2면 2줄만 있어도 됨
        for b in range(10):
            if b==0:
                dp[a][b] = dp[a-1][b+1]
            elif b==9:
                dp[a][b] = dp[a-1][b-1]
            else:
                dp[a][b] = dp[a-1][b-1] + dp[a-1][b+1]    
print(sum(dp[n-1])%1000000000)


