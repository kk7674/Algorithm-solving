import sys
input = sys.stdin.readline
n = int(input())
s= [0,1,1,2]

if n > 3:
    for i in range(4, n+1):
        s.append(s[i-1] + s[i-2])
print(s[n])


