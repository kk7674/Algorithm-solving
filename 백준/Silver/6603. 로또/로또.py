import sys
input = sys.stdin.readline

rs = [0]*7
def recur(start, cnt): #6개만 뽑는 거임
    if cnt == 6:
        for i in range(6):
            print(rs[i], end =' ')
        print()
        return
    for i in range(start,length):
        rs[cnt] = arr[i]
        recur(i+1,cnt+1)



while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        exit()
    del arr[0]
    length = len(arr)
    recur(0,0)
    print()
