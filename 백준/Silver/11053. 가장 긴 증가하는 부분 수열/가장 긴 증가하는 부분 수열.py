import sys
input = sys.stdin.readline
n = int(input())
d = [1] * n
num = list(map(int, input().split()))
for i in range(n):
    for j in range(i):
        if num[i] > num[j]:
            #최댓값을 구하는 것
            d[i] = max(d[i], d[j]+1)

print(max(d))