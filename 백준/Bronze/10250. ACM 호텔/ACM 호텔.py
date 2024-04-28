T = int(input())

for _ in range(T):
    H,W,N = map(int, input().split())

    floor = N % H
    d = (N//H) +1

    if floor == 0:
        d -= 1
        floor = H

    print(floor*100+d)