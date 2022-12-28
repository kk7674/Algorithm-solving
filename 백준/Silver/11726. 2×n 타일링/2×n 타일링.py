import sys
input = sys.stdin.readline
d = [0]*1001
d[1] = 1
d[2] = 2
d[3] = 3
n = int(input())
if n>3:
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2]
print(d[n] % 10007)