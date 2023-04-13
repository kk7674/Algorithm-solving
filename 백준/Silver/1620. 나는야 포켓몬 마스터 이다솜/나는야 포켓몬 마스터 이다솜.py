import sys
input = sys.stdin.readline

n,m = map(int,input().split())#총 포켓몬 수, 문제 수
dic = {}
for i in range(1,n+1):
    a = input().rstrip()
    dic[i] = a
    dic[a] = i

for i in range(m):
    p = input().rstrip()
    if p.isdigit():
        print(dic[int(p)])
    else:
        print(dic[p])


