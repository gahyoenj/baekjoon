N,C = map(int,input().split())
home = []
for _ in range(N):
    x = int(input())
    home.append(x)

home.sort()

start = 1
end = home[-1]-home[0]

while start <= end:
    mid = (start+end) // 2
    cnt = 1
    install = home[0]

    for i in range(1,N):
        if home[i] - install >= mid:
            cnt += 1
            install = home[i]

    if cnt >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)