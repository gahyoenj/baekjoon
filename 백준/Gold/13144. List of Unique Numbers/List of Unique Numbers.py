N = int(input())
arr = list(map(int,input().split()))

start = 0
end = 0
cnt = 0
can = set()

while end < N:
    while end < N and arr[end] not in can:
        can.add(arr[end])
        cnt += (end-start + 1)
        end += 1

    can.remove(arr[start])
    start += 1

print(cnt)