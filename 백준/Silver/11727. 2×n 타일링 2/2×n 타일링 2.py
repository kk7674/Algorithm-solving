import sys
input = sys.stdin.readline

n = int(input())
s= [0,1,3,5]

if n >=4:
    for i in range(4, n+1):
        s.append(s[i-2]*2 + s[i-1])
print(s[n] % 10007)

