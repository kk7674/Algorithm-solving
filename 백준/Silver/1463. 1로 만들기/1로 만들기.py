import sys
input = sys.stdin.readline
n = int(input())
d = [0]*1000001
#d[1] = 0
#2부터 시작하면 될듯
for i in range(2,n+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
print(d[n])