def solution(n):
    #F(0) = 0
    #F(1) = 1
    #F(2) = F(0) + F(1) = 1
    #F(3) = F(1) + F(2) = 2
    dp = []
    dp.append(0)
    dp.append(1)    
    answer = 0
    
    for i in range(2,n+1):
        dp.append(dp[i-1] + dp[i-2])
    answer = dp[n] % 1234567
    
    
    
    
    
    return answer