import sys
from collections import deque
input = sys.stdin.readline
queue = deque([])

ex = []
n = int(input())
lists1 = []
printing = []
for i in range(n):
    queue.append(int(input())) # 43687521
#queue[0]
num = 1
i = 0
flag = 0
while True:  
    if len(ex) != 0:
        if queue[0] == ex[-1]:
            ex.pop()
            queue.popleft()
            printing.append('-')
            flag = 1
        
    if flag != 1 and queue[0] != num:
        ex.append(num)
        printing.append('+')
        flag = 2
    elif flag != 1 and queue[0] == num:
        queue.popleft()
        printing.append('+')
        printing.append('-')
        flag = 2
    
    if flag != 1:
        num+=1

    flag = 0

    if len(queue) == 0:
        break
    
    if len(ex) != 0:
        if ex[-1] > n:
            print("NO")
            exit(0)
for i in printing:
    print(i)