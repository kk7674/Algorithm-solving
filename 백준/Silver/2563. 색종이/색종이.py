import sys
input = sys.stdin.readline

n = int(input())
arr = [[0 for _ in range(100)] for _ in range(100)]
cnt = 0

for _ in range(n):
 a,b = map(int,input().split())
 for i in range(10):
     for j in range(10):
        arr[a+i][b+j] = 1

for i in arr:
 for j in i:
     if j == 1:
         cnt+=1
print(cnt)

