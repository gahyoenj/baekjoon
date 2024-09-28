H, W = map(int, input().split())

lst = list(map(int,input().split()))

rain = 0

for idx in range(W):
    if idx-1 >= 0:
        if lst[idx] < lst[idx-1]:
            cnt = 0
            for i in range(idx+1,W):
                if lst[i] >= lst[idx-1]:
                    cnt += 1
                    break
            if cnt > 0:
                rain += (lst[idx-1] - lst[idx])
                lst[idx] = lst[idx-1]
            if cnt ==0:
                x = max(lst[idx::])
                rain += (x-lst[idx])
                lst[idx] =x

print(rain)