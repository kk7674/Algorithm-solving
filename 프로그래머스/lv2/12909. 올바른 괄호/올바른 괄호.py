from collections import deque
def solution(s):
    queue = deque()
    for i in s:
        if i == '(':
            queue.append(i)
        else:
            if queue:
                queue.pop()
            else:
                return False
    if queue:
        return False
    else:
        return True
                