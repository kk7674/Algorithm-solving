def solution(babbling):
    answer = 0
    for item in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w*2 not in item:
                item = item.replace(w,' ')         
        if len(item.strip()) == 0:
                answer+=1    
    return answer