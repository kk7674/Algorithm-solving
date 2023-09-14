import sys
input = sys.stdin.readline

n = int(input())
len_org = int(input())
org = input().rstrip()
cmp = "IOI"
cnt = 0
if n != 1:
    for i in range(n-1):
        cmp += "OI"
length = len(cmp)
for i in range(len_org-length+1):
    if cmp == org[i:i+length]:
        cnt+=1
print(cnt)

