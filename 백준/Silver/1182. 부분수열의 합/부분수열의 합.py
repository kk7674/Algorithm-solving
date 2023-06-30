import sys
input = sys.stdin.readline

m,n = map(int,input().split()) #정수 개수, 원하는 합
arr = list(map(int,input().split()))
ans = 0
def recur(depth,T_sum):
    global ans
    if depth ==  m:
        return
    val = arr[depth]
    T_sum += val
    if T_sum == n:
        ans+=1
    recur(depth+1,T_sum)
    recur(depth + 1, T_sum-val)

recur(0,0)
print(ans)