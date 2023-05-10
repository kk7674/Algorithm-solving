import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        if len(heap) != 0:
            print(heapq.heappop(heap))
        else: #길이가 0이면
            print(0)
