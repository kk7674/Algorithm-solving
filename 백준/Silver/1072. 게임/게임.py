import sys
input = sys.stdin.readline
x,y = map(int, input().split())
z = (y * 100) // x
if z >= 99:
    print(-1)
else:
    answer = 0
    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2
        if (y+mid)*100 // (x+mid) > z: #확률이 상승
            answer = mid
            right = mid - 1
        else: #확률이 작아졌거나 변경없는 경우
            left = mid+1
    print(answer)

