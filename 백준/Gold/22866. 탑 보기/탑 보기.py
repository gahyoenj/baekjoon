
N = int(input())
building = list(map(int, input().split()))


can = [[0, 0, 0] for _ in range(N)]


stack = []
for i in range(N):

    while stack and stack[-1][0] <= building[i]:
        stack.pop()

    can[i][0] = len(stack)
    if stack:
        can[i][2] = stack[-1][1] + 1
    stack.append((building[i], i))

stack = []
for i in range(N - 1, -1, -1):
    while stack and stack[-1][0] <= building[i]:
        stack.pop()

    can[i][1] = len(stack)
    # print(i,stack)
    if stack:
        if can[i][2] == 0:
            can[i][2] = stack[-1][1] + 1
        else:
            if abs(can[i][2] - 1 - i) > abs(stack[-1][1] - i):
                can[i][2] = stack[-1][1] + 1
    stack.append((building[i], i))

for l,r,n in can:
    if l+r == 0:
        print(0)
    else:
        print(l+r,n)
