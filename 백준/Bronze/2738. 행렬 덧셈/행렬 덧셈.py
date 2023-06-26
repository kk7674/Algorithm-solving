import sys
input = sys.stdin.readline
a,b = map(int, input().split())

arr1 = [list(map(int,input().split())) for _ in range(a)]

arr2 = [list(map(int,input().split())) for _ in range(a)]

temp = [[0 for _ in range(b)] for _ in range(a)]

for i in range(a): #행
    for j in range(b): #열
        temp[i][j] = arr1[i][j] + arr2[i][j]

for i in temp:
    print(*i)


