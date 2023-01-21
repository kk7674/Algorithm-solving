import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
total = int(input())

start, end = 0, max(arr)

while start <= end:
    mid = (start+ end)//2
    tmp_sum = 0
    for item in arr:
        tmp_sum += min(item,mid)

    if tmp_sum > total:# 위시 sum이 정부 돈보다 많을 경우는 답이 될 수 없음
        end = mid - 1
    else:#정부예산이 많은 경우
        start = mid + 1
        answer = mid

print(answer)
