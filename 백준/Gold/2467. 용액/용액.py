n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

left = 0
right = n-1

answer = abs(arr[left] + arr[right]) #양 끝단을 더한값의 절댓값을 기준값으로
final = [arr[left], arr[right]] #저장소

while left < right: #같아지면 안되니까
    left_val = arr[left]
    right_val = arr[right]

    sum = left_val + right_val

    if abs(sum) < answer:
        answer = abs(sum)
        final = [left_val, right_val]
        if answer == 0:
            break
    if sum < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])
