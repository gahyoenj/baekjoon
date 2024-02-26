A, B = map(int,input().split())
Q = [4,7]
cnt = 0
while Q:
    F = Q[0]
    Q.pop(0)

    if  F <= B:
        if A <= F:
            cnt += 1
        Q.append(F*10+4)
        Q.append(F*10+7)
print(cnt)