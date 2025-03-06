def push(light,cnt):
    for i in range(1,N-1):
        if light[i-1] != make[i-1]:
            for j in range(i-1,i+2):
                if light[j] == 0:
                    light[j] = 1
                else:
                    light[j] = 0
            cnt += 1
    if light[-1] != make[-1]:
        cnt += 1
        for i in range(-2,0):
            if light[i] == 0:
                light[i] = 1
            else:
                light[i] = 0

    if light == make:
        return cnt
    else:
        return -1

N = int(input())
current = list(map(int,input()))
make = list(map(int,input()))

bulbs = current[::]
for i in range(2):
    if bulbs[i] == 0:
        bulbs[i] = 1
    else:
        bulbs[i] = 0

if current == make:
    print(0)
else:
    count = push(current,0)
    if count != -1:
        print(count)
    else:
        count = push(bulbs,1)
        if count !=-1:
            print(count)
        else:
            print(-1)