import sys
input = sys.stdin.readline
d = [0] * 11 #해당 수에 도달하는 방법의 개수
d[1] = 1 
d[2] = 2
d[3] = 4
n = int(input())
for i in range(n):
    case = int(input()) 
    if case > 3:
        for j in range(4, case+1):
            d[j] = d[j-3] + d[j-2] + d[j-1]    
    print(d[case])


    
