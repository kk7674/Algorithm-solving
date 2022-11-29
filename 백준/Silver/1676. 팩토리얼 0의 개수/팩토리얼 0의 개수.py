import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

def facto(n: int):
    if n ==1:
        return 1

    total = 1
    for _ in range(1, n+1):
        total *= n
        n -= 1
    return total

cnt = 0
num = facto(N)
arr = deque(list(map(int,str(num))))
while True:
    if len(arr) != 0:
        if arr.pop() == 0:
            cnt += 1
        else:
            print(cnt)
            break
    else:
        print(cnt)
        break


