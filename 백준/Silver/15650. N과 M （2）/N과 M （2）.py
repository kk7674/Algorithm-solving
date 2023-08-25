import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [i for i in range(1,n+1)]
if m == 1:
    for item in arr:
        print(item)
else:
    c = combinations(arr,m)
    temp = list(c)
    for item in temp:
        print(*item)
    

