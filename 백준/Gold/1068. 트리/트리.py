import sys
input = sys.stdin.readline
n = int(input())
tree = list(map(int, input().split()))
d = int(input())
cnt = 0
def delete(d):
    tree[d] = -2
    for i in range(n):
        if tree[i] == d: #없애려는 노드가 부모일 경우
            delete(i)

delete(d)
for i in range(n):
    if tree[i] != -2 and i not in tree: #부모가 없어지지 않았고 누군가의 부모가 아닌 경우
        cnt+=1
print(cnt)
