import sys
input = sys.stdin.readline
temp_max = 0
temp_i = 0
temp_j = 0
arr = [list(map(int,input().split())) for _ in range(9)]
for i in range(9):
    for j in range(9):
        if arr[i][j] > temp_max:
            temp_max = arr[i][j]
            temp_i = i
            temp_j = j
print(temp_max)
print(temp_i+1, temp_j+1)

