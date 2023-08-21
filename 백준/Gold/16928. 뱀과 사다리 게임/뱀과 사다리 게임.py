from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(1)
    ok[1] = 1
    while q:
        now = q.popleft() #기준점
        for i in range(1,7): #1~6
            next_move = now + i
            if next_move <= 100 and not ok[next_move]: #100 초과 -> break                
                if next_move in ladder.keys():
                    next_move = ladder[next_move]                            
                elif next_move in snake.keys():
                    next_move = snake[next_move]                                                                
                if ok[next_move] == 0:
                    q.append(next_move)
                    ok[next_move] = 1 #방문처리
                    cnt[next_move] = cnt[now] + 1
  
a,b = map(int,input().split())
ladder = dict()
snake = dict()
cnt = [0]*101 #칸마다 횟수 카운트
ok = [0]*101 #방문 횟수

for _ in range(a):
    i,j = map(int,input().split())
    ladder[i] = j
for _ in range(b):
    i,j = map(int,input().split())
    snake[i] = j
bfs()
print(cnt[100])