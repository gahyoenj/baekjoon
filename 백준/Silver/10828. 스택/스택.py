import sys
N = int(sys.stdin.readline())
STACK = []
for _ in range(N):
    s = sys.stdin.readline().strip()
    if 'push' in s:
        push = s.split()
        STACK.append(int(push[1]))
    if s == 'top':
        if STACK:
            print(STACK[-1])
        else:
            print(-1)
    if s == 'pop':
        if STACK:
            result = STACK.pop()
            print(result)
        else:
            print(-1)
    if s == 'size':
        print(len(STACK))
    if s == 'empty':
        if STACK:
            print(0)
        else:
            print(1)