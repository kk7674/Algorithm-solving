import sys
input = sys.stdin.readline
n = int(input())

d = [list(map(int, input().split())) for _ in range(n)]

 # 0번째 idx(1번째 집)는 확인x 1번째 idx(2번째 집)부터 최적의 값을 해당 배열에 갱신
for i in range(1, n):
    d[i][0] += min(d[i-1][1], d[i-1][2])
    d[i][1] += min(d[i-1][0], d[i-1][2])
    d[i][2] += min(d[i-1][0], d[i-1][1])
print(min(d[n-1]))

