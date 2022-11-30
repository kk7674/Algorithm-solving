import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())

def facto1(n : int , m : int): #분자용
    total = 1
    for _ in range(m):
        total *= n
        n -= 1
    return total

def facto2(m : int): #분모용
    total = 1
    for _ in range(m):
        total *= m
        m -= 1
    return total 

print(facto1(n, m) // facto2(m))