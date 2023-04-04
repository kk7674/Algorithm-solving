import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    q = deque()
    q.append((x1,y1)) #집 좌표
    while q:
        r1,r2 = q.popleft() #집, 편의점..
        if abs(p1-r1) + abs(p2-r2) <= 1000:
            print("happy")
            return

        for i in range(n):
            if not ok[i]:
                c1, c2 = cs[i] #새로운 편의점
                if abs(r1-c1) + abs(r2-c2) <= 1000:
                    q.append((c1, c2))
                    ok[i] = True
    print("sad")
    return

T = int(input())
for _ in range(T):
    n = int(input()) #편의점 수
    x1,y1 = map(int,input().split()) #집 좌표
    cs = []
    for _ in range(n): #편의점 입력받기
        x2,y2 = map(int,input().split())
        cs.append((x2,y2)) #편의점 리스트
    p1,p2 = map(int,input().split())
    ok = [False for _ in range(n+1)] #편의점 방문
    bfs()





