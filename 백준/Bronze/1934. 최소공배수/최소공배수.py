import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a,b = map(int, input().split())
    x = 1
    for i in range(max(a,b),0,-1):
        if a % i == 0 and b % i == 0:
            x = i
            break

    print(a*b//x)
