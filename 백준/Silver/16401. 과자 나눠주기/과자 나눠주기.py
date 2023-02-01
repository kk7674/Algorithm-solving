# 4 3
# 1 15(max)
# mid로 전체 과자를 나눴을 떄 몫의 합이 조카수보다 큰 경우?
import sys
input = sys.stdin.readline
m,n = map(int,input().split())
arr = list(map(int,input().split()))

answer = 0
left = 1
right = max(arr)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for item in arr:
        cnt += item // mid
    if cnt >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)


