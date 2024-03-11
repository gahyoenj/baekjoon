import sys
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    s,e = map(int, sys.stdin.readline().split())
    lst.append((s,e))

lst.sort(key=lambda x:(x[1],x[0]))
# print(lst)

cnt = 1
e = lst[0][1]
for i in range(1,N):   # while 문 활용했더니 시간초과
    if lst[i][0] >= e:   # 끝나는 시간이 다음 회의 시작보다 작으면 회의 가능
        cnt += 1
        e = lst[i][1]
print(cnt)
