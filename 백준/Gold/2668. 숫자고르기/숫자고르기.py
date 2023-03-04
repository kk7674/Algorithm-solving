import sys
sys.setrecursionlimit(1000000)
n = int(input())
arr = [0] #0번 idx에 0 val 넣어주기
result = set([])
for _ in range(n):
    arr.append(int(input()))

def dfs(top, bottom, start):#idx집합, val 집합, 시작포인트
    top.add(start)
    bottom.add(arr[start])
    if arr[start] in top: #꼬리잡기 성공
        if top == bottom:
            result.update(top)
            return True
        return False #꼬리 잡기 성공했는데 위 아래 다르면 False
    #꼬리 잡기 실패
    return dfs(top,bottom,arr[start])

for i in range(1,n+1):
    if i not in result:
        dfs(set(),set(),i)

print(len(result))
print(*sorted(list(result)), sep='\n')

