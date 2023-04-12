import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    result = 1
    dic = {}
    n = int(input())
    for _ in range(n):
        a,b = map(str,input().split()) # 디테일, 종류
        if b not in dic.keys():
            dic[b] = set()
            dic[b].add(a)
        else:
            dic[b].add(a)
    for i in dic.keys():
        result *= (len(dic[i])+1)
    print(result-1)
