while True:
    n = int(input())
    if n == 0 : break
    else:
        s = str(n)
        if s == s[::-1]:
            print('yes')
        else:
            print('no')