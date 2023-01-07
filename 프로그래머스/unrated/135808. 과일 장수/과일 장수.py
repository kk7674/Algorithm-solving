def solution(k, m, score):
    answer = 0
    length = len(score)    
    score.sort(reverse = True)
    for i in range(0, length, m): #length = 7, m=4 len - m < m
        if length - i < m:
            break
        answer += min(score[i:i+m]) * m
                             
    return answer
    


#3322111