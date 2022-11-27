import sys
N, M = map(int,sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in trees:
        if i > mid:
            total += i-mid
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)





