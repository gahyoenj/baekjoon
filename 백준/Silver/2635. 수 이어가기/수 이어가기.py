N = int(input())
max_lst = []
for i in range(1,N+1):
    lst = [N]
    lst.append(i)

    idx = 1
    while True:
        num = lst[idx-1] - lst[idx]
        if num < 0:
            break
        lst.append(num)
        idx += 1

    if len(max_lst) < len(lst):
        max_lst = lst
print(len(max_lst))
print(*max_lst)