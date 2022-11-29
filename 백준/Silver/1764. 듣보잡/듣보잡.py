import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
temp_n = []
temp_m = []
human = []
cnt = 0

def b_search(target: str, arr: list):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return target
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0

for _ in range(n):
    temp_n.append(str(input()))
temp_n.sort()

for _ in range(m):
    temp_m.append(str(input()))
temp_m.sort()

for i in range(m):
    temp = b_search(temp_m[i], temp_n)
    if temp != 0:
        human.append(temp)
        cnt += 1
        
print(cnt)
for i in human:
    print(i, end='')

    