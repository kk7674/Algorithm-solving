import sys
input = sys.stdin.readline
n = input()
arr1 = list(map(int, input().split()))

m = input()
arr2 = list(map(int, input().split()))

def find(arr, target):
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1


arr1.sort()
for item in arr2:
    if find(arr1, item) == 1:
        print(1, end=" ")
    else:
        print(0, end=" ")






