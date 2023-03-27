import sys
from collections import deque
input = sys.stdin.readline

#전체, 현재, 목적지, 업, 다운
f,s,g,u,d = map(int,input().split())

#경우의 수 방문처리 리스트
ok = [False] * (f+1)
count = [0 for _ in range(f+1)]

def bfs():
    queue = deque([s])
    ok[s] = True
    while queue:        
        v = queue.popleft()
        if v == g:
            print(count[g])
            exit()
        for i in (v+u,v-d): # 2, -1
            if 0 < i <= f and not ok[i]:
                ok[i] = True
                count[i] = count[v] + 1
                queue.append(i) # queue에서 뽑은 값 + 업
                
bfs()
print("use the stairs")