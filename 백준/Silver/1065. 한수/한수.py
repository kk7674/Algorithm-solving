#1~99까진 무조건
#100이상일땐 100으로 나눈 몫 a, 나머지를 10으로 나눈 몫 b 나머지 c
n= int(input()) #110
cnt = 0
for i in range(1,n+1):
    if i < 100:
        cnt += 1
    else:
        nums = list(map(int,str(i)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            cnt+=1
print(cnt)





