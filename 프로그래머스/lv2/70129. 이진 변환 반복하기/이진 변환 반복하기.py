def solution(s):
    answer = []
    cnt1 = 0 #제거 0
    cnt2 = 0 #회차
    while s != '1':
        length = len(s)
        s = s.replace('0','')
        cnt1 += length - len(s)
        s = bin(len(s))
        s = s[2:]
        cnt2+=1
    answer.append(cnt2)
    answer.append(cnt1)
    return answer