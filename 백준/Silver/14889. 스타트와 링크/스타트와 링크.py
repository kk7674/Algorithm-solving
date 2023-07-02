#조합을 뽑고 나서 나머지 집합은 뽑히지않은 거로
#set 자료형에 - 연산을 사용한다면?
import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
mini = sys.maxsize
temp = set([])
for i in range(1,n+1):
    temp.add(i)

arr = [list(map(int,input().split())) for _ in range(n)]

for item in combinations(range(1,n+1),n//2):
    total1 = 0
    total2 = 0
    item_1 = list(set(item))
    item_2 = list(temp-set(item_1))    
    for r1 in combinations(item_1,2):
        total1 += arr[r1[0]-1][r1[1]-1]
        total1 += arr[r1[1]-1][r1[0]-1]

    for r2 in combinations(item_2,2):
        total2 += arr[r2[0]-1][r2[1]-1]
        total2 += arr[r2[1]-1][r2[0]-1]

    cal = abs(total1-total2)
    
    if  cal < mini:
        mini = cal

print(mini)
    
    
