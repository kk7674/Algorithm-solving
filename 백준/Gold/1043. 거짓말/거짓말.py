import sys
input = sys.stdin.readline
h, p  = map(int, input().split()) #사람, 파티
T = set(input().split()[1:])
arr = []
cnt = 0

for _ in range(p):
    arr.append(set(input().split()[1:]))

for i in range(p):
    for party in arr: # T와 party 비교    
        if party & T:#겹치는게 있으면
            T = party | T

for party in arr: # T와 party 비교    
    if not party & T:#겹치는게 없으면
        cnt += 1
print(cnt)
       
