N = int(input())
arr = list(map(int, input().split()))

cnt = 1
maxV = 1
for idx in range(N-1):
    if arr[idx] <= arr[idx+1]:
        cnt += 1
    else:
        cnt = 1
    if cnt > maxV:
        maxV = cnt
cnt = 1
for idx in range(1,N):
    if arr[idx-1] >= arr[idx]:
        cnt += 1
    else:
        cnt = 1
    if cnt > maxV:
        maxV = cnt


print(maxV)