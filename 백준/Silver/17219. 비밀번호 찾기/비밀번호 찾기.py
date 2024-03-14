import sys
N, M = map(int, sys.stdin.readline().split())
password = {}
for _ in range(N):
    com, pwd = map(str, sys.stdin.readline().split())
    password[com] = pwd

# print(password)
result = []
for _ in range(M):
    ans = sys.stdin.readline().rstrip()
    print(password[ans])

