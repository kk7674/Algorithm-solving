#top down
#목표수 기준 끝에 1이 있으면 없애고 없으면 나누기 2
#해서 a값 나오면 연산 횟수 출력
#안나오면 -1 출력
import sys
input = sys.stdin.readline
a, b = map(int,input().split())
cnt = 0
while b != a:
    temp = b
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2

    if temp == b:
        print(-1)
        exit(0)
    cnt+=1
print(cnt+1)
