N = int(input())
number = list(map(int,input().split()))

number.sort()

cnt = 0

for i in range(N):
    start = 0
    end = N-1

    target = number[i]
    while start < end:

        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue

        if number[start] + number[end] == target:
            cnt += 1
            break

        if number[start] + number[end] < target:
            start += 1

        else:
            end -= 1



print(cnt)