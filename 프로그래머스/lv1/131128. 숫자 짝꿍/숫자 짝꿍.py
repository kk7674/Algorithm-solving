def solution(X, Y):    
    answer = ''
    numx = {str(n):0 for n in range(10)}
    numy = {str(n):0 for n in range(10)}
    temp = []
    cnt = 0
    for x in X:
        numx[x] += 1
    for y in Y:
        numy[y] += 1
        
    for k in range(9,-1,-1):
        k = str(k)
        iternum = min(numx[k], numy[k])
        
        if iternum != 0:
            cnt+=1
            
        if k == '0':        
            if temp != []:                        
                for _ in range(iternum):
                    temp.append(k)
        else:
            for _ in range(iternum):
                    temp.append(k)
        
    answer = ''.join(temp)
    if answer == "":
        if cnt != 0:
            answer = "0"
        else:
            answer = "-1"
    
    return answer