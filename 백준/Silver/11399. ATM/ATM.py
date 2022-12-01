import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

sum = 0
length = len(arr)
for idx, val in enumerate(arr):
    sum += val * (length - idx)
print(sum)