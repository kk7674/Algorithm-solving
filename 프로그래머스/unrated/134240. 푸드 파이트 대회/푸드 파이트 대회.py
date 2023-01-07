def solution(food):
    temp = []
    temp2 = []        
    len_food = len(food)

    for i in range(1, len_food):
        num = (food[i]) // 2
        for _ in range(num):
            temp.append(i)

    for item in temp:
        temp2.append(item)
    temp2.append(0)
    temp.reverse()
    for item in temp:
        temp2.append(item)
    answer = ''.join(str(item) for item in temp2)    
    

    return answer