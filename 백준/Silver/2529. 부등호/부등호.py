import sys
input = sys.stdin.readline
n = int(input()) #부등호 개수
arr = list(map(str, input().split()))
maxi = -sys.maxsize
mini = sys.maxsize
maxi_s = ''
mini_s = ''
#n+1만큼 숫자를 뽑아서 부등호와 비교. n/ n+1  (부등호수, 뽑을 숫자)
visit = [False] * 10 #0~9까지 10개
temp = []
def recur(depth): #depth <- 몇개 뽑았는지

    global maxi, maxi_s,mini,mini_s
    if depth == n+1: #다 뽑으면
        #부등호 뽑아내서 비교
        for i in range(n): #예를 들어 숫자가 3개가 나올 경우, 01 12 일케 2개씩 뽑아서 ㄱ
            if arr[i] == '<' and temp[i] >= temp[i+1]: #잘못된 경우
                return
            elif arr[i] == '>' and temp[i] <= temp[i+1]: #잘못된 경우
                return
        num = ''.join(map(str, temp))
        if int(num) > maxi:
            maxi = int(num)
            maxi_s = num
        if int(num) < mini:
            mini = int(num)
            mini_s = num
        return

    for i in range(10): #0~9까지 뽑
        if not visit[i]:
            visit[i] = True
            temp.append(i)
            recur(depth+1)
            temp.pop()
            visit[i] = False
recur(0)
print(maxi_s)
print(mini_s)








