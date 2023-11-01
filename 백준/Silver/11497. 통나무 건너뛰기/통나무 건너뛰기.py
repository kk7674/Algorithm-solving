import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()    
    mini = -sys.maxsize
    temp = [0 for _ in range(n)]        
    i,j = 0,0

    for _ in range(n//2):        
        temp[j] = arr[i]
        temp[-(j+1)] = arr[i+1]
        i+=2
        j+=1
    if n%2 != 0:
        temp[n//2] = arr[-1]    

    for j in range(n):
        mini = max(mini,abs(temp[j] - temp[j-1]))
    print(mini)