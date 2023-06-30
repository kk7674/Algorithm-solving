#파훼 방법
#주어진 카드 중 몇가지의 카드를 선택하는지가 유동적이므로
#반복문의 범위로 사용하면 되고 맨처음 카드의 수를 문자로 받고
#조합 별로 join으로 합친 다음, int형으로 변환.
#해당 정수가 결과리스트 저장 여부를 확인 후 최종 개수 도출
import sys
input = sys.stdin.readline
arr = [-1] #주어진 카드 담는 통
temp = []
rs = set([]) #최종 
n = int(input()) #카드수
ok = [False] * (n+1) #방문 여부
m = int(input()) #몇장 선택

for _ in range(n):
    arr.append(int(input().rstrip()))


def btrack(num):
    if num == m:
        rs.add(''.join(map(str,temp)))
        return
    for i in range(1,n+1):
        if not ok[i]:
            ok[i] = True
            temp.append(arr[i])
            btrack(num+1)
            ok[i] = False
            temp.pop()

btrack(0)

print(len(rs))
