def R_calc(arr):
    max_len = 0
    for row in range(len(arr)):
        result = []
        num_lst = set(arr[row])
        if 0 in num_lst:
            num_lst.remove(0)

        for num in num_lst:
            cnt = arr[row].count(num)
            if (num,cnt) not in result:
                result.append((num,cnt))
        result.sort(key=lambda x:(x[1],x[0]))
        lst = []
        for x,y in result:
            lst.extend([x,y])
        arr[row] = lst
        max_len = max(max_len,len(lst))

    for row in arr:
        while len(row) < max_len:
            row.append(0)

        if len(row) > 100:
            del row[100:]

    return arr

def C_calc(arr):
    max_len = 0
    col_arr = list(zip(*arr))
    # print(col_arr)
    new_arr = []
    for col in col_arr:
        result = []
        num_lst = set(col)
        if 0 in num_lst:
            num_lst.remove(0)
        # print(col)
        for num in num_lst:
            cnt = col.count(num)
            result.append((num,cnt))
            # print(result)
        result.sort(key=lambda x: (x[1], x[0]))
        # print(result)
        lst = []
        for x, y in result:
            lst.extend([x, y])
        new_arr.append(lst)
        max_len = max(max_len, len(lst))
    # print(new_arr)
    for i in range(len(new_arr)):
        while len(new_arr[i]) < max_len:
            new_arr[i].append(0)

        if len(new_arr[i]) > 100:
            del new_arr[i][100:]

    result = list(zip(*new_arr))
    # print(result)
    ans = [list(row) for row in result]
    # print(ans)
    return ans


r,c,k = map(int,input().split())

A = []

for _ in range(3):
    a = list(map(int,input().split()))
    A.append(a)
time = 0
flag = False
while time <= 100:
    if 0 <= r-1 < len(A) and 0 <= c-1 < len(A[0]):
        if A[r-1][c-1] == k:
            flag = True
            print(time)
            break

    if len(A) >= len(A[0]):
        A = R_calc(A)

    else:
        A = C_calc(A)

    time += 1

if not flag:
    print(-1)