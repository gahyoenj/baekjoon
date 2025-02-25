N = int(input())

building = list(map(int,input().split()))

laser = [0] * N
stack = []

for i in range(N):
    while stack:
        top = stack[-1][1]
        if top >= building[i]:
            break
        stack.pop()

    if stack:
        laser[i] = stack[-1][0]
    stack.append((i+1,building[i]))

print(*laser)