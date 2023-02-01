# min(arr) ~ 1000000
# mid값으로 각 스태프 풍선 부는 시간을 나눈 몫의 합이 M이랑 같으면

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))

left = (m//n) * min(arr)
right = (m//n+1) * max(arr)
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for item in arr:
        cnt += mid // item
    if cnt >= m:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)
