def opposite(op):
    for g in op:
        twelve = g[0]
        g[0:7] = g[1:8]
        g[-1] = twelve

def clock(cl):
    for g in cl:
        eleven = g[-1]
        g[1:8] = g[0:7]
        g[0] = eleven



gear = [list(input()) for _ in range(4)]

K = int(input())
for _ in range(K):
    op = []
    cl = []
    i,d = map(int,input().split())
    direction = d
    for idx in range(i,4):
        if gear[idx-1][2] != gear[idx][-2]:
            if direction == -1:
                cl.append(gear[idx])
                direction = 1
            elif direction == 1:
                op.append(gear[idx])
                direction = -1
        else:
            break

    direction = d
    for idx in range(i,1,-1):
        if gear[idx-1][-2] != gear[idx-2][2]:
            if direction == -1:
                cl.append(gear[idx-2])
                direction = 1
            elif direction == 1:
                op.append(gear[idx-2])
                direction = -1
        else:
            break

    if d == -1:
        op.append(gear[i-1])
    if d == 1:
        cl.append(gear[i-1])

    # print(op)
    # print(cl)
    opposite(op)
    clock(cl)
    # print(gear)
ans = 0
for i in range(4):
    if gear[i][0] == '1':
        ans += (2**i)

print(ans)