"""
괄호 역할이 사실상 -를 무효화 할 수 있다는 점.

30 - 100 + 55 - 50 + 40

"""
import sys
start = 0
num = []
Eq = input().split('-')

for item in Eq:
        temp = list(map(int,item.split('+')))
        num.append(sum(temp))

if len(Eq) >= 2:    
    start = num[0]
    num.pop(0)
    for i in num:
        start -= i
    print(start)
else:
     print(sum(num))