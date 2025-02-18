N = input()
l = len(N)

if l == 1 and int(N)+1 <10:
    print(int(N)+1)

elif N == '9':
    print(11)
else:
    if l % 2 == 0:
        left = N[:l//2]
    else:
        left = N[:((l//2)+1)]

    check = left + N[:(l//2)][::-1]

    if int(check) > int(N):
        print(check)
    else:
        next = int(left) + 1
        if len(str(next)) == len(left):
            if l % 2 == 0:
                check = str(next) + str(next)[::-1]
            else:
                check = str(next) + str(next)[:l//2][::-1]
        else:
            next = int(N[:l//2]) + 1
            if l % 2 == 0:
                check = str(next) + str(next)[:(len(str(next))-1)][::-1]
            else:
                check = str(next) + str(next)[::-1]
        print(check)