"""

딕셔너리 느낌으로 원래 주어진 수의 
idx를 저장.

{2:0, 4:[1,3], -10:2, -9:4}
key 기준으로 오름차순 정렬
{-10:2, -9:4, 2:0, 4:[1,3]}
걍 딕셔너리 각 key를 조회할때 변수하나 ++ 해줘서 idx 대체.
idx값 따로 저장하는 temp 만들고 append하면 될듯?

"""
import sys
input = sys.stdin.readline
from collections import defaultdict
n = int(input())
arr = list(map(int,input().split()))
dic = defaultdict(list)

for i in range(n):
    v = arr[i]    
    dic[v].append(i)

d = sorted(dic.items())
d = dict(d)
temp = 0
result = [0 for _ in range(n)]
for key,val in d.items():
    for item in val:
        result[item] = temp
    temp+=1
print(*result)







