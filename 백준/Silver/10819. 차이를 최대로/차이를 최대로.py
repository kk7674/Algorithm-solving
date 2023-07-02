#순열 문제이다.
#순열 조합을 뽑아보고 해당 연산 수행하고 max값 갱신.
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
visit = [False] * (n+1)
rs = []
maxi = -sys.maxsize
def recur(depth):
    global maxi
    if depth == n: #0부터 시작하니까 n이 되면 오바 재귀
        temp = 0
        for i in range(n-1): # n이 6이면 0~4
            temp += abs(rs[i] - rs[i+1])
        maxi = max(maxi, temp)        
        return
    
    for i in range(n): #방문처리와 리스트에 해당 값 넣어주기
        if not visit[i]:
            rs.append(arr[i])
            visit[i] = True
            recur(depth+1)
            visit[i] = False
            rs.pop()

recur(0)
print(maxi)
