import sys
from collections import deque

N =int(sys.stdin.readline())
queue = deque([])

for _ in range(N):
    ord = list(sys.stdin.readline().split())
    if len(ord) == 2:
        if ord[0] == 'push':
            queue.appendleft(int(ord[1])) #좌측(앞)에 삽입
    else: # 길이가 1일 경우
        if ord[0] == 'pop':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.pop())
        elif ord[0] == 'size':
            print(len(queue))
        elif ord[0] == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif ord[0] == 'front':
            if len(queue) !=0:
                print(queue[-1])
            else:
                print(-1)
        elif ord[0] == 'back':
            if len(queue) !=0:
                print(queue[0])
            else:
                print(-1)
        ord.clear()