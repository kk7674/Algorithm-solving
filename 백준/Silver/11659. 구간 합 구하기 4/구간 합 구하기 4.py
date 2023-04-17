import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
sum = [0]

total = 0
for i in arr:
    total += i
    sum.append(total)
for _ in range(m):
    a,b = map(int,input().split())
    print(sum[b] - sum[a-1])






