def solution(s):
    cnt1, cnt2 = 0, 0
    answer = 0
    len_s = len(s)
    standard = 0
    
    for i in range(len_s):
        if standard == 0:
            standard = s[i]
                        
        if standard == s[i]:
            cnt1+=1
        else:
            cnt2+=1
            
        if cnt1 == cnt2:
            answer+=1
            cnt1, cnt2 = 0,0
            standard = 0
        elif cnt1 != cnt2:
            if i == len_s - 1:
                return answer+1
        
    return answer