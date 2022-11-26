import sys
from collections import Counter

N =int(int(sys.stdin.readline()))
temp = {}
lists1 = []
for _ in range(N):
    lists1.append(int(sys.stdin.readline()))
    
lists1.sort()

#산술 평균
print(round(sum(lists1)/N)) #첫째줄

#print(dict(sorted(temp.items(), key = lambda x:x[1])))
#print(max(temp.keys(), key = lambda k : temp[k]))
#print(temp, key= temp.get)

#중앙값
print(lists1[N//2]) #소수점 제외

#최빈값
cnt = Counter(lists1).most_common()
mode = []
for i in cnt:
    if i[1] >= cnt[0][1]:
        mode.append(i[0])
    else:
        break
if len(mode) == 1: #
    print(mode[0])
else:
    mode.sort() #오름차순 sort
    print(mode[1]) # 2번째로 작은 수 출력

#범위
print(lists1[-1] - lists1[0])
