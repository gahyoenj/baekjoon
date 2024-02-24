N = int(input())
ballon = list(map(int, input().split()))
ballon_i = [i for i in range(1,N+1)]
i = 0
ans = []
current = ballon.pop(0)
ans.append(ballon_i.pop(i))
while ballon:
    if current <0:
        i = (i+current)%len(ballon)
    else:
        i = (i+current-1)%len(ballon)
    current = ballon.pop(i)
    ans.append(ballon_i.pop(i))
print(*ans)