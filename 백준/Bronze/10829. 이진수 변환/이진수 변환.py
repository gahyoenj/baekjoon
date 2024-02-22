def decTobin(value):
    s =''
    while value > 0:
        s = str(int(value%2)) + s
        value //= 2
    return s

N = int(input())
print(decTobin(N))