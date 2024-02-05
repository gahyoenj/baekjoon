while True:
    n = int(input())

    lst = [1]
    my_lst =[]
    if n == -1:
        break
    else:
        for d in range(2, n):
            if n % d ==0:
                q = n //d
                r = d
                lst.append(q)
                lst.append(r)

    my_set = set(lst)
    for i in my_set:
        my_lst.append(i)
    if n != sum(my_set):
        print(f'{n} is NOT perfect.')
    else:
        my_lst.sort()
        print(f'{n} =', end=' ')
        for i in range(len(my_lst)-1):
            print(f'{my_lst[i]} +', end=' ')
        print(my_lst[-1])