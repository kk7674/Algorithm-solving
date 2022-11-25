import sys
from collections import deque

N = int(sys.stdin.readline())

ord = 0
for i in range(N):
    cnt, idx = map(int,sys.stdin.readline().split())            
    #list                    
    lists1 = list(map(int,sys.stdin.readline().split()))
    temp = lists1[idx] 
    lists1[idx] = [lists1[idx],1]    
    #deque
    queue = deque(lists1.copy()) 
    lists1[idx] = temp    #list 2차원배열 제거
    maxi = max(lists1)

    while True:        
        #첫번째가 최댓값이 아니고 최댓값이 뽑아낼라하는거 보다 큼
        if type(queue[0]) == int:
            if queue[0] != maxi:
                queue.rotate(-1)                                                           
            else:                
                lists1.remove(queue[0]) #해당값 리스트에서 제거
                queue.popleft()
                maxi = max(lists1)                        
                ord+=1 #뽑아내기 카운트
        else: #타입이 리스트일경우 (핵심) 뽑아낼 경우
            if queue[0][0] != maxi and maxi > temp:
                queue.rotate(-1) 
            #마지막 핵심 뽑아내기    
            elif queue[0][0] == maxi and maxi == temp:
                ord+=1
                print(ord)
                ord = 0
                #lists1.clear()
                break    
            #첫번째가 최댓값인 경우 뽑아내기        
            else:
                lists1.remove(queue[0]) #해당값 리스트에서 제거
                queue.popleft()    
                maxi = max(lists1)                    
                ord+=1 #뽑아내기 카운트
        




  