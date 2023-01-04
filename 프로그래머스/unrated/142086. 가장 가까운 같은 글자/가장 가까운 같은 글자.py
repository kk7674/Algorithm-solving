def solution(s):
    answer = []
    alphabet = {}
    idx=0
    for item in s:
        if item not in alphabet:
            answer.append(-1)
        else:
            answer.append(abs(alphabet[item] - idx))
            
        alphabet[item] = idx        
        idx+=1
        
    return answer