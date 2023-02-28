import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n= int(input())
arr= [[] *0 for i in range(n+1)] #n이 7이면 7까지 0~7
visited = [0] * (n+1) #8개 만들기 0~7

def dfs(s):
    for i in arr[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)

for _ in range(n-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(1)

for i in range(2,n+1): #2~7
    print(visited[i])

