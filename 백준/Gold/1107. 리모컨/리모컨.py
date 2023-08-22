import sys
input = sys.stdin.readline

target = int(input())
n = int(input())
break_btn  = list(map(str,input().split()))
mini = abs(target - 100)

for num in range(1000001):
    str_num = str(num)
    length = len(str_num)
    for i in range(length):
        if str_num[i] in break_btn:
            break
        if i == length-1:
            mini = min(mini, abs(target - num) + length)
print(mini)

