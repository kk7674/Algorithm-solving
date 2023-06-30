import sys
input = sys.stdin.readline

M,N = map(int,input().split()) #총 카드 수, 합 결과
arr = list(map(int,input().split()))

def dfs(depth,sum_T):
    global ans

    if depth == M:
        return
    
    sum_T += arr[depth]

    if sum_T == N:
        ans+=1
    
    dfs(depth + 1, sum_T - arr[depth])
    dfs(depth + 1, sum_T)


ans = 0
dfs(0,0)
print(ans)
