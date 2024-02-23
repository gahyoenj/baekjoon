import sys
from collections import deque
N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    order = sys.stdin.readline().strip()
    if 'push' in order:
        push = order.split()
        q.append(int(push[1]))
    if order == 'pop':
        if q:
            x = q.popleft()
            print(x)
        else:
            print(-1)
    if order == 'size':
        print(len(q))
    if order == 'empty':
        if q:
            print(0)
        else:
            print(1)
    if order == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    if order == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
