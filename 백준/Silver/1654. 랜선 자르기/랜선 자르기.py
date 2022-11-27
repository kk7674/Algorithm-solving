import sys
N, M = map(int,sys.stdin.readline().split())
lan = []
for i in range(N):
    lan.append(int(sys.stdin.readline()))

start = 0
end = max(lan)
res = 0

while start <= end:
    if start == 0 and end == 1:
        mid = 1
    elif start == 0 and end == 0:
        break
    else:
        mid = (start + end)//2

    total = 0

    for i in lan:
        total += i // mid
    if total >= M:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)

