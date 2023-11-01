import sys
input = sys.stdin.readline
N, T = map(int,input().split())
arr = list(map(int, input().split()))

for _ in range(T):
    arr.sort()
    a = arr[0]
    b = arr[1]
    arr[0],arr[1] = a+b,a+b
print(sum(arr))