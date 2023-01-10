def solution(n):
    answer = 0
    cnt1 = 0
    cnt2 = 0
    while True:        
        arr1 = bin(n)
        arr1 = arr1[2:]
        
        for i in arr1:
            if i == '1':
                cnt1+=1
                
        temp = n+1
        arr2 = bin(temp)
        arr2 = arr2[2:]
        
        for i in arr2:
            if i == '1':
                cnt2+=1
        if cnt1 == cnt2:
            return n+1        
        
        temp = 0
        n+=1
