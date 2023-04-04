import sys
from collections import deque

def bfs(start, end):    
    q = deque()
    q.append((start,0)) #노드, 누적 거리
    
    ok = [False] * (n+1)
    ok[start] = True

    while q:
        nd, d = q.popleft()

        if nd == end: #최종 목적지와 큐에서 꺼낸 노드 값이 같으면
            return d #누적 거리 출력
        for i, j in arr[nd]: #노드, 거리            
            if not ok[i]:
                q.append((i,d+j))
                ok[i] = True


n, m = map(int,input().split())
arr = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, d = map(int,input().split())
    arr[a].append((b,d))
    arr[b].append((a,d))

for _ in range(m):
    s,e = map(int,input().split())
    print(bfs(s,e))


